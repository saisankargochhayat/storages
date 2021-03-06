"""Added ExternalSoftwareEnvironment, ExternalHardwareInformation, constraints for syncs

Revision ID: 9a8ce1e52efb
Revises: f60593780969
Create Date: 2019-10-07 07:40:32.070193+00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9a8ce1e52efb'
down_revision = 'f60593780969'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('external_hardware_information',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cpu_vendor', sa.Integer(), nullable=True),
    sa.Column('cpu_model', sa.Integer(), nullable=True),
    sa.Column('cpu_cores', sa.Integer(), nullable=True),
    sa.Column('cpu_model_name', sa.String(length=256), nullable=True),
    sa.Column('cpu_family', sa.Integer(), nullable=True),
    sa.Column('cpu_physical_cpus', sa.Integer(), nullable=True),
    sa.Column('gpu_model_name', sa.String(length=256), nullable=True),
    sa.Column('gpu_vendor', sa.String(length=256), nullable=True),
    sa.Column('gpu_cores', sa.Integer(), nullable=True),
    sa.Column('gpu_memory_size', sa.Integer(), nullable=True),
    sa.Column('ram_size', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('external_software_environment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('environment_name', sa.String(length=256), nullable=True),
    sa.Column('python_version', sa.String(length=256), nullable=True),
    sa.Column('image_name', sa.String(length=256), nullable=True),
    sa.Column('image_sha', sa.String(length=256), nullable=True),
    sa.Column('os_name', sa.String(length=256), nullable=True),
    sa.Column('os_version', sa.String(length=256), nullable=True),
    sa.Column('cuda_version', sa.String(length=256), nullable=True),
    sa.Column('environment_type', postgresql.ENUM('RUNTIME', 'BUILDTIME', name='environment_type'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('adviser_run', sa.Column('external_build_software_environment_id', sa.Integer(), nullable=True))
    op.add_column('adviser_run', sa.Column('external_hardware_information_id', sa.Integer(), nullable=True))
    op.add_column('adviser_run', sa.Column('external_run_software_environment_id', sa.Integer(), nullable=True))
    op.drop_constraint('adviser_run_user_build_software_environment_id_fkey', 'adviser_run', type_='foreignkey')
    op.drop_constraint('adviser_run_user_run_software_environment_id_fkey', 'adviser_run', type_='foreignkey')
    op.drop_constraint('adviser_run_hardware_information_id_fkey', 'adviser_run', type_='foreignkey')
    op.create_foreign_key(None, 'adviser_run', 'external_software_environment', ['external_run_software_environment_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'adviser_run', 'external_software_environment', ['external_build_software_environment_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'adviser_run', 'external_hardware_information', ['external_hardware_information_id'], ['id'], ondelete='CASCADE')
    op.drop_column('adviser_run', 'user_build_software_environment_id')
    op.drop_column('adviser_run', 'user_run_software_environment_id')
    op.drop_column('adviser_run', 'hardware_information_id')
    op.drop_column('hardware_information', 'is_user')
    op.alter_column('python_package_version', 'os_name',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.alter_column('python_package_version', 'os_version',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.alter_column('python_package_version', 'python_version',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.drop_column('software_environment', 'is_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('software_environment', sa.Column('is_user', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.alter_column('python_package_version', 'python_version',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.alter_column('python_package_version', 'os_version',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.alter_column('python_package_version', 'os_name',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.add_column('hardware_information', sa.Column('is_user', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('adviser_run', sa.Column('hardware_information_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('adviser_run', sa.Column('user_run_software_environment_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('adviser_run', sa.Column('user_build_software_environment_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'adviser_run', type_='foreignkey')
    op.drop_constraint(None, 'adviser_run', type_='foreignkey')
    op.drop_constraint(None, 'adviser_run', type_='foreignkey')
    op.create_foreign_key('adviser_run_hardware_information_id_fkey', 'adviser_run', 'hardware_information', ['hardware_information_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('adviser_run_user_run_software_environment_id_fkey', 'adviser_run', 'software_environment', ['user_run_software_environment_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('adviser_run_user_build_software_environment_id_fkey', 'adviser_run', 'software_environment', ['user_build_software_environment_id'], ['id'], ondelete='CASCADE')
    op.drop_column('adviser_run', 'external_run_software_environment_id')
    op.drop_column('adviser_run', 'external_hardware_information_id')
    op.drop_column('adviser_run', 'external_build_software_environment_id')
    op.drop_table('external_software_environment')
    op.drop_table('external_hardware_information')
    # ### end Alembic commands ###
