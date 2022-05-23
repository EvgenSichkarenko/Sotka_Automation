from model.model_registr_secretary import ModelSecretary
import datetime

email = "secreatry" + datetime.datetime.now().strftime("%Y_%H_%M_%S") + "@zetmail.com"

regisrt_secr = [ModelSecretary(
    secr_email=email,
    secr_fullname="Rita QA",
),
                   # ...
                   ]