import sqlalchemy
from sqlalchemy import MetaData, Table, Column, \
    Integer, String, TIMESTAMP, ForeignKey, JSON,\
    Boolean
from datetime import datetime

metadata = MetaData()

# primary_key=True уникальное значение перыичный ключь
# nullable=False означает что запрещено значение null, none

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

# TIMESTAMP, default=datetime.utcnow это время когда была \
# сделана регистрация
# внешений ключь на таблицу id
# "role_id" сылается на верхнию таблицу role
# "password" hech пароль

user =Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("role.c.id")),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),

)

# alembic init migrations применяем команду в терминале

# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata=create_all(engine)

