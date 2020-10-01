from app import db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand

#manager = Manager(app)
migrate = Migrate(db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(db = db,Role = Role, User = User)

if __name__ == '__main__':
    manager.run(debug=True)