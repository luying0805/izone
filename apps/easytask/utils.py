# -*- coding: utf-8 -*-


class TaskResponse(object):
    def __init__(self, code=0, data=None, message="", error=""):
        self.code = code
        self.data = data or {}
        self.message = message
        self.error = error

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def as_dict(self):
        data = {
            'code': self.code,
            'data': self.data,
            'message': self.message,
            'error': self.error
        }
        return data


class ErrorTaskResponse(TaskResponse):
    def __init__(self, code=1, data=None, message="", error=""):
        super(ErrorTaskResponse, self).__init__(code, data, message, error)


if __name__ == '__main__':
    response = TaskResponse()
    response.data = {'result': "xx"}
    print(response)
