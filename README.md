# pyrdstation

[![Build Status](https://travis-ci.org/JetBov/pyrdstation.svg?branch=master)](https://travis-ci.org/JetBov/pyrdstation)
[![codecov.io](https://codecov.io/github/hbetts/orbitalpy/coverage.svg?branch=master)](https://codecov.io/github/JetBov/pyrdstation?branch=master)

This project aims to create a small lib to interact with Resultados Digitais RDStation API.

## Installation

```bash
pip install -e git+https://github.com/JetBov/pyrdstation.git#egg=pyrdstation
```

## Usage

```python
  from pyrdstation.client import Lead, RDClient

  lead = Lead(email="user@server.com", conversion_id="converted-on-github")
  lead.name = "Lead Name"
  lead.job_position = "Job Position"
  lead.company = "Lead Company"
  lead.employee_qty = 100
  lead.company_address = "Lead Address"
  lead.phone = "+1 702 555-5555"
  lead.mobile = "+1 702 555-5544"
  lead.website = "www.leadsite.com"
  lead.twitter = "@leadTwitter"
  lead.c_utmz = "google tag"
  lead.tags = "LEAD TAGS"
  
  client = RDClient(token="<your public RDStation token>")
  try:
      response = client.track_conversion(lead, traffic_source="Your Source")
      print response
  except Exception as e:
      print e.message
```

For more information, check [Resultados Digitais Conversion API documentation](http://ajuda.rdstation.com.br/hc/pt-br/sections/200626689-Integrações-com-Sistema-Próprio-via-API-).

## Contributing

Read [CONTRIBUTING](CONTRIBUTING.md).
