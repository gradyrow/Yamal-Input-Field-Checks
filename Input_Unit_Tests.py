import unittest
from Check_Yaml import *


class TestCheckYaml(unittest.TestCase):

    def test_host_input(self):
        self.assertIsNone(hostInput("169.0.0.4"))
        # Test invalid input
        with self.assertRaises(ValueError):
            hostInput("invalid_host")

    def test_state_input(self):
        self.assertIsNone(stateInput("present"))
        # Test invalid input
        with self.assertRaises(ValueError):
            stateInput("invalid_state")

    def test_name_subject_input(self):
        self.assertIsNone(nameSubjectInput("Home Host Server"))
        # Test invalid input
        with self.assertRaises(ValueError):
            nameSubjectInput("invalid_!name||")

    def test_port_input(self):
        self.assertIsNone(portInput("2556"))
        # Test invalid input
        with self.assertRaises(ValueError):
            portInput("invalid_port")

    def test_email_input(self):
        self.assertIsNone(emailInput("gradyrow@hotmail.com"))
        # Test invalid input
        with self.assertRaises(ValueError):
            emailInput("invalid_email")

    def test_body_msg_input(self):
        self.assertIsNone(bodyMsgInput('"This is and email notification"'))
        # Test invalid input
        with self.assertRaises(ValueError):
            bodyMsgInput("invalid_body_msg")

    def test_command_input(self):
        self.assertIsNone(commandInput("echo 'Hello from Ansible' > /tmp/output.txt"))
        # Test invalid input
        with self.assertRaises(ValueError):
            commandInput("invalid_command||")

    def test_count_input(self):
        self.assertIsNone(countInput("1"))
        # Test invalid input
        with self.assertRaises(ValueError):
            countInput("invalid_count")

    def test_unit_input(self):
        self.assertIsNone(unitInput("minutes"))
        # Test invalid input
        with self.assertRaises(ValueError):
            unitInput("invalid_unit")

    def test_timespec_input(self):
        self.assertIsNone(timespecInput("now + 12 hours"))
        self.assertIsNone(timespecInput("2300"))
        self.assertIsNone(timespecInput("201807012300"))
        self.assertIsNone(timespecInput("2018-07-01T23:00"))
        # Test invalid input
        with self.assertRaises(ValueError):
            timespecInput("invalid_timespec")

    def test_repo_input(self):
        self.assertIsNone(repoInput('https://github.com/example/repo.git'))
        # Test invalid input
        with self.assertRaises(ValueError):
            repoInput("invalid_repo")

    def test_dest_input(self):
        self.assertIsNone(destInput('/path/to/the/destination'))
        # Test invalid input
        with self.assertRaises(ValueError):
            destInput("invalid_dest")


if __name__ == '__main__':
    unittest.main()
