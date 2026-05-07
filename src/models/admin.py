from tortoise import fields

from schemas.menus import MenuType

from .base import BaseModel, TimestampMixin
from .enums import MethodType


class User(BaseModel, TimestampMixin):
    username = fields.CharField(
        max_length=20, unique=True, description="User Name", index=True
    )
    alias = fields.CharField(max_length=30, null=True, description="Full Name", index=True)
    email = fields.CharField(
        max_length=255, unique=True, description="Email", index=True
    )
    phone = fields.CharField(max_length=20, null=True, description="Phone", index=True)
    password = fields.CharField(max_length=128, null=True, description="Password")
    is_active = fields.BooleanField(default=True, description="Is Active", index=True)
    is_superuser = fields.BooleanField(
        default=False, description="Is Superuser", index=True
    )
    last_login = fields.DatetimeField(null=True, description="Last Login Time", index=True)
    roles = fields.ManyToManyField("models.Role", related_name="user_roles")
    dept_id = fields.IntField(null=True, description="Department ID", index=True)

    class Meta:
        table = "user"


class Role(BaseModel, TimestampMixin):
    name = fields.CharField(
        max_length=20, unique=True, description="Role Name", index=True
    )
    desc = fields.CharField(max_length=500, null=True, description="Role Description")
    menus = fields.ManyToManyField("models.Menu", related_name="role_menus")
    apis = fields.ManyToManyField("models.Api", related_name="role_apis")

    class Meta:
        table = "role"


class Api(BaseModel, TimestampMixin):
    path = fields.CharField(max_length=100, description="API Path", index=True)
    method = fields.CharEnumField(MethodType, description="Request Method", index=True)
    summary = fields.CharField(max_length=500, description="Request Summary", index=True)
    tags = fields.CharField(max_length=100, description="API Tags", index=True)

    class Meta:
        table = "api"


class Menu(BaseModel, TimestampMixin):
    name = fields.CharField(max_length=20, description="Menu Name", index=True)
    remark = fields.JSONField(null=True, description="Reserved Field")
    menu_type = fields.CharEnumField(MenuType, null=True, description="Menu Type")
    icon = fields.CharField(max_length=100, null=True, description="Menu Icon")
    path = fields.CharField(max_length=100, description="Menu Path", index=True)
    order = fields.IntField(default=0, description="Sort Order", index=True)
    parent_id = fields.IntField(default=0, description="Parent Menu ID", index=True)
    is_hidden = fields.BooleanField(default=False, description="Is Hidden")
    component = fields.CharField(max_length=100, description="Component")
    keepalive = fields.BooleanField(default=True, description="Keep Alive")
    redirect = fields.CharField(max_length=100, null=True, description="Redirect")

    class Meta:
        table = "menu"


class Dept(BaseModel, TimestampMixin):
    name = fields.CharField(
        max_length=20, unique=True, description="Department Name", index=True
    )
    desc = fields.CharField(max_length=500, null=True, description="Remarks")
    is_deleted = fields.BooleanField(
        default=False, description="Soft Delete Flag", index=True
    )
    order = fields.IntField(default=0, description="Sort Order", index=True)
    parent_id = fields.IntField(
        default=0, max_length=10, description="Parent Department ID", index=True
    )

    class Meta:
        table = "dept"


class DeptClosure(BaseModel, TimestampMixin):
    ancestor = fields.IntField(description="Ancestor", index=True)
    descendant = fields.IntField(description="Descendant", index=True)
    level = fields.IntField(default=0, description="Depth", index=True)


class AuditLog(BaseModel, TimestampMixin):
    user_id = fields.IntField(description="User ID", index=True)
    username = fields.CharField(
        max_length=64, default="", description="User Name", index=True
    )
    module = fields.CharField(
        max_length=64, default="", description="Module", index=True
    )
    summary = fields.CharField(
        max_length=128, default="", description="Request Description", index=True
    )
    method = fields.CharField(
        max_length=10, default="", description="Request Method", index=True
    )
    path = fields.CharField(
        max_length=255, default="", description="Request Path", index=True
    )
    status = fields.IntField(default=-1, description="Status Code", index=True)
    response_time = fields.IntField(
        default=0, description="Response Time (ms)", index=True
    )
    request_args = fields.JSONField(null=True, description="Request Params")
    response_body = fields.JSONField(null=True, description="Response Body")

    class Meta:
        table = "audit_log"


class FileMapping(BaseModel, TimestampMixin):
    """File Mapping Model - Manage mapping relationship between file ID and file information"""

    file_id = fields.CharField(
        max_length=255, unique=True, description="File ID", index=True
    )
    original_filename = fields.CharField(max_length=255, description="Original Filename")
    file_type = fields.CharField(max_length=50, description="File Type")
    file_size = fields.BigIntField(null=True, description="File Size (bytes)")
    upload_user_id = fields.IntField(description="Upload User ID", index=True)
    file_path = fields.CharField(max_length=500, null=True, description="Local File Path")

    class Meta:
        table = "file_mapping"
