class ErrorForm:

    def get_errors(self):
        """ Return list of validation errors
            or False, if errors isn't exists. """
        errors_list = []
        for _, errors in self.errors.items():
            for error in errors:
                errors_list.append(error)
        if len(errors_list) <= 0:
            return False
        else:
            return errors_list

    def is_has_errors(self):
        """ Returns True if form has errors
            and False if errors isn't exists """
        if len(self.errors) > 0:
            return True

        return False
