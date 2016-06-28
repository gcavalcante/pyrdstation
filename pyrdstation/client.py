"""
A simple rdstation client class
"""
import json
import requests


__author__ = 'zamboni'


class Lead(object):
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value
    
    @property
    def conversion_id(self):
        return self._conversion_id

    @conversion_id.setter
    def conversion_id(self, value):
        self._conversion_id = value

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def job_position(self):
        return self._job_position
    
    @job_position.setter
    def job_position(self, value):
        self._job_position = value
    
    @property
    def company(self):
        return self._company
    
    @company.setter
    def company(self, value):
        self._company = value
    
    @property
    def employee_qty(self):
        return self._employee_qty
    
    @employee_qty.setter
    def employee_qty(self, value):
        self._employee_qty = value
    
    @property
    def company_address(self):
        return self._company_address
    
    @company_address.setter
    def company_address(self, value):
        self._company_address = value
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        self._phone = value
    
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value

    @property
    def website(self):
        return self._website

    @website.setter
    def website(self, value):
        self._website = value

    @property
    def twitter(self):
        return self._twitter

    @twitter.setter
    def twitter(self, value):
        self._twitter = value

    @property
    def c_utmz(self):
        return self._c_utmz

    @c_utmz.setter
    def c_utmz(self, value):
        self._c_utmz = value

    @property
    def tags(self):
        return self._tags
    
    @tags.setter
    def tags(self, value):
        self._tags = value
    
    def __init__(self, email=None, conversion_id=None, name=None, job_position=None, company=None, employee_qty=None,
                 company_address=None, phone=None, mobile=None, website=None, twitter=None, c_utmz=None, tags=None):
        if conversion_id is None:
            raise ValueError("conversion_id was not provided.")
        if email is None:
            raise ValueError("error was not provided.")
        self._email = email
        self._conversion_id = conversion_id
        self._name = name
        self._job_position = job_position
        self._company = company
        self._employee_qty = employee_qty
        self._company_address = company_address
        self._phone = phone
        self._mobile = mobile
        self._website = website
        self._twitter = twitter
        self._c_utmz = c_utmz
        self._tags = tags

    def to_dict(self):
        if self._conversion_id is None:
            raise ValueError("conversion_id was not provided.")
        if self._email is None:
            raise ValueError("error was not provided.")

        dict_value = {
            "identificador": self._conversion_id,
            "email": self._email
        }
        if self._name is not None:
            dict_value.update({"nome": self._name})
        if self._job_position is not None:
            dict_value.update({"cargo": self._job_position})
        if self._company is not None:
            dict_value.update({"empresa": self._company})
        if self._employee_qty is not None:
            dict_value.update({"numero-de-funcionarios": self._employee_qty})
        if self._company_address is not None:
            dict_value.update({"endereco-empresa": self._company_address})
        if self._phone is not None:
            dict_value.update({"telefone": self._phone})
        if self._mobile is not None:
            dict_value.update({"celular": self._mobile})
        if self._website is not None:
            dict_value.update({"website": self._website})
        if self._twitter is not None:
            dict_value.update({"twitter": self._twitter})
        if self._c_utmz is not None:
            dict_value.update({"c_utmz": self._c_utmz})
        if self._tags is not None:
            dict_value.update({"tags": self._tags})
        return dict_value

    def to_rdstation_json(self, token_rdstation=None):
        if token_rdstation is not None:
            dict_value = self.to_dict()
            dict_value.update({"token_rdstation": token_rdstation})

            if 'numero-de-funcionarios' in dict_value.keys() and isinstance(self._employee_qty, int):
                dict_value['numero-de-funcionarios'] = str(self._employee_qty)

            return json.dumps(dict_value, sort_keys=True)
        else:
            raise ValueError('token_rdstation was not provided')


class RDClient(object):
    _rdstation_url = "https://www.rdstation.com.br/api/1.3/conversions"

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value

    @property
    def private_token(self):
        return self._private_token

    @private_token.setter
    def private_token(self, value):
        self._private_token = value

    def __init__(self, token=None, private_token=None):
        if token is not None:
            self._token = token
        if private_token is not None:
            self._private_token = private_token

    def track_conversion(self, lead=None):
        """
        track a conversion on RDStation
        :param lead: Lead
        :return: None
        """
        assert isinstance(lead, Lead)
        if self._token is None:
            raise ValueError('No RDStation Token has been provided.')

        json_to_post = lead.to_rdstation_json(token_rdstation=self._token)

        headers = {
            "Content-type": "application/json"
        }

        try:
            request = requests.post(self._rdstation_url, headers=headers, data=json_to_post)
        except requests.ConnectionError as e:
            raise StandardError("Error on track conversion. ConnectionError return: %s" % e.message)

        if request.status_code != requests.codes.ok:
            raise StandardError("Error on track conversion. return: %s" % request.reason)

