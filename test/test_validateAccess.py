from home.utils import ValidateAccess, Patient, Doctor, Person


class TestValidateAccess:

    def test_check_valid_cpf(self):
        user = ValidateAccess(None,
                              'email.123@gmail.com',
                              'G@z23Kda(',
                              'G@z23Kda(',
                              '137.751.310-60',
                              '7833213',
                              '23-54-2003',
                              True)

        assert user.validate_cpf()

    def test_check_invalid_cpf(self):
        user = ValidateAccess(None,
                              'email.123@gmail.com',
                              'G@z23Kda(',
                              'G@z23Kda(',
                              '111.111.111-11',
                              '7833213',
                              '23-54-2003',
                              True)

        assert user.validate_cpf() is False

    def test_check_valid_sus(self):
        user = ValidateAccess(None,
                              'email.123@gmail.com',
                              'G@z23Kda(',
                              'G@z23Kda(',
                              '137.751.310-60',
                              '7833213',
                              '23-54-2003',
                              True)

        assert user.validate_sus()

    def test_check_invalid_sus(self):
        user = ValidateAccess(None,
                              'email.123@gmail.com',
                              'G@z23Kda(',
                              'G@z23Kda(',
                              '137.751.310-60',
                              '2833213',
                              '23-54-2003',
                              True)

        assert user.validate_sus() is False

    def test_check_valid_birthday(self):
        user = ValidateAccess(None,
                              'email.123@gmail.com',
                              'G@z23Kda(',
                              'G@z23Kda(',
                              '137.751.310-60',
                              '7833213',
                              '2023-12-2',
                              True)

        assert user.validate_birthday()

    def test_check_invalid_birthday(self):
        user = ValidateAccess(None,
                              'email.123@gmail.com',
                              'G@z23Kda(',
                              'G@z23Kda(',
                              '137.751.310-60',
                              '7833213',
                              '2024-12-2',
                              True)

        assert user.validate_birthday() is False

    def test_check_valid_password(self):
        user = ValidateAccess(None,
                              'email.123@gmail.com',
                              '12345678',
                              '12345678',
                              '137.751.310-60',
                              '7833213',
                              '23-54-2003',
                              True)

        assert user.validate_password()

    def test_check_valid_different_password(self):
        user = ValidateAccess(None,
                              'email.123@gmail.com',
                              '12345678',
                              '12345674',
                              '137.751.310-60',
                              '7833213',
                              '23-54-2003',
                              True)

        assert user.validate_password() is False

    def test_check_password_length(self):
        user = ValidateAccess(None,
                              'email.123@gmail.com',
                              '1234',
                              '1234',
                              '137.751.310-60',
                              '7833213',
                              '23-54-2003',
                              True)

        assert user.validate_password() is False

    def test_check_valid_email(self):
        access = ValidateAccess(None,
                                'email.123@gmail.com',
                                'G@z23Kda(',
                                'G@z23Kda(',
                                '11111111111',
                                '7833213',
                                '23-54-2003',
                                True)

        assert access.validate_email()

    def test_check_invalid_email(self):
        access = ValidateAccess(None,
                                'email.123gmail.com',
                                'G@z23Kda(',
                                'G@z23Kda(',
                                '11111111111',
                                '7833213',
                                '23-54-2003',
                                True)

        assert access.validate_email() is not True

    def test_patient_object(self):
        paciente = Patient("Joaquim",
                           "email@gmail.com",
                           "12345678",
                           "36738219",
                           "78234234",
                           "Masculino",
                           "2003-06-10")

        assert isinstance(paciente, Patient)

    def test_patient_subclass(self):
        paciente = Patient("Joaquim",
                           "email@gmail.com",
                           "12345678",
                           "36738219",
                           "78234234",
                           "Masculino",
                           "2003-06-10")

        assert isinstance(paciente, Person)

    def test_doctor_object(self):
        doutor = Doctor("Joaquim",
                        "email@gmail.com",
                        "12345678",
                        "36738219",
                        "78234234",
                        "Masculino",
                        "2003-06-10",
                        "321312")

        assert isinstance(doutor, Doctor)

    def test_doctor_subclass(self):
        doutor = Doctor("Joaquim",
                        "email@gmail.com",
                        "12345678",
                        "36738219",
                        "78234234",
                        "Masculino",
                        "2003-06-10",
                        "321312")

        assert isinstance(doutor, Person)
