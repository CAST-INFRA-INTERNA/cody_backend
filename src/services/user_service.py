"""User service layer - unified user business logic"""

from tortoise.expressions import Q

from repositories.dept import dept_repository
from repositories.user import user_repository
from schemas.base import Fail, Success, SuccessExtra
from schemas.users import UserCreate, UserUpdate
from services.base_service import BaseService
from utils.cache import cached, clear_user_cache


class UserService(BaseService):
    """User service class - handles user-related business logic"""

    def __init__(self):
        super().__init__(user_repository)

    async def get_user_list(
        self,
        page: int = 1,
        page_size: int = 10,
        username: str = "",
        email: str = "",
        dept_id: int | None = None,
    ) -> SuccessExtra:
        """Get user list - with search filters and department info association"""
        try:
            # Build search filter conditions
            search_filters = self._build_user_search_filters(
                username=username, email=email, dept_id=dept_id
            )

            # Get paginated data
            total, items = await self.repository.list(
                page=page,
                page_size=page_size,
                search=search_filters,
                order=["-created_at"],
            )

            # Transform data and associate department info
            data = await self._transform_user_list_with_dept(items)

            return SuccessExtra(data=data, total=total, page=page, page_size=page_size)

        except Exception as e:
            self.logger.error(f"Failed to get user list: {str(e)}")
            return Fail(msg="Failed to get user list")

    @cached("user_detail", ttl=300)
    async def get_user_detail(self, user_id: int) -> Success:
        """Get user detail - with cache"""
        try:
            user_obj = await user_repository.get(id=user_id)
            if not user_obj:
                return Fail(msg="User not found")

            user_dict = await user_obj.to_dict(m2m=True, exclude_fields=["password"])
            return Success(data=user_dict)

        except Exception as e:
            self.logger.error(f"Failed to get user detail: {str(e)}")
            return Fail(msg="Failed to get user detail")

    async def create_user(self, user_in: UserCreate) -> Success:
        """Create user - with email uniqueness check and role assignment"""
        try:
            # Check if email already exists
            existing_user = await user_repository.get_by_email(user_in.email)
            if existing_user:
                return Fail(
                    code=400,
                    msg="The user with this email already exists in the system.",
                )

            # Create user
            new_user = await user_repository.create_user(obj_in=user_in)

            # Update user roles
            await user_repository.update_roles(new_user, user_in.role_ids)

            return Success(msg="Created Successfully")

        except Exception as e:
            self.logger.error(f"Failed to create user: {str(e)}")
            return Fail(msg="Failed to create user")

    async def update_user(self, user_in: UserUpdate) -> Success:
        """Update user - with role update and cache clearing"""
        try:
            # Update user basic info
            user = await user_repository.update(id=user_in.id, obj_in=user_in)

            # Update user roles
            await user_repository.update_roles(user, user_in.role_ids)

            # Clear related cache
            await clear_user_cache(user_in.id)

            return Success(msg="Updated Successfully")

        except Exception as e:
            self.logger.error(f"Failed to update user: {str(e)}")
            return Fail(msg="Failed to update user")

    async def delete_user(self, user_id: int) -> Success:
        """Delete user - with cache clearing"""
        try:
            await user_repository.remove(id=user_id)

            # Clear related cache
            await clear_user_cache(user_id)

            return Success(msg="Deleted Successfully")

        except Exception as e:
            self.logger.error(f"Failed to delete user: {str(e)}")
            return Fail(msg="Failed to delete user")

    async def reset_user_password(self, user_id: int) -> Success:
        """Reset user password"""
        try:
            await user_repository.reset_password(user_id)
            return Success(msg="Password has been reset")

        except Exception as e:
            self.logger.error(f"Failed to reset password: {str(e)}")
            return Fail(msg="Failed to reset password")

    def _build_user_search_filters(
        self,
        username: str = "",
        email: str = "",
        dept_id: int | None = None,
    ) -> Q:
        """Build user search filter conditions"""
        filters = Q()

        if username:
            filters &= Q(username__contains=username)

        if email:
            filters &= Q(email__contains=email)

        if dept_id is not None:
            filters &= Q(dept_id=dept_id)

        return filters

    async def _transform_user_list_with_dept(self, items) -> list[dict]:
        """Transform user list data and associate department info"""
        data = []

        for obj in items:
            # Transform user data, exclude password field
            user_dict = await obj.to_dict(m2m=True, exclude_fields=["password"])

            # Associate department info
            dept_id = user_dict.pop("dept_id", None)
            if dept_id:
                dept_obj = await dept_repository.get(id=dept_id)
                user_dict["dept"] = await dept_obj.to_dict() if dept_obj else {}
            else:
                user_dict["dept"] = {}

            data.append(user_dict)

        return data


# Global instance
user_service = UserService()
