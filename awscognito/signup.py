import boto3
import hmac
import hashlib
import base64
from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from backend import user
from awscognito import sendmail

USER_POOL_ID = 'eu-west-1_vZqAAJiUV'
CLIENT_ID = '29o6b1mgrifo46mj5rmb720djf'
CLIENT_SECRET = 'qqn4beh5pd2bu6l2804l2nv86si7apgru31ejhrvakenjlf3vds'
REGION = 'eu-west-1'


def handler(request, creates, db:Session):
    
    def get_secret_hash(username):
        msg = username + CLIENT_ID
        dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'),
                       msg=str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
        d2 = base64.b64encode(dig).decode()
        return d2

    def lambda_handler(event, context):
        for field in ["email", "password","given_name","company_name","tenant_id","role","account_name","title","country",
                      "line_manager","address","department","job_title","cell_number","level_twomanager","date_of_birth","start_date"
                      "town","postcode"]:
            # print(field)
            pass

        #         if not event.get(field):
        #             return {"error": False, "success": True, 'message': f"{field} is not present", "data": None}
        # print(event)
        email = event['email']
        password = event['password']
        given_name = event['given_name']
        company_name = event['company_name']
        tenant_id = event['tenant_id']
        role = event['role']
        account_name = event['account_name']
        title = event['title']
        country = event['country']
        line_manager = event['line_manager']
        address = event['address']
        department =event['department']
        job_title = event['job_title']
        level_twomanager = event['level_twomanager']
        cell_number=event['cell_number']
        date_of_birth=event['date_of_birth']
        start_date=event['start_date']
        town=event['town']
        postcode=event['postcode']

        client = boto3.client('cognito-idp', 'eu-west-1')
        
        try:
            resp = client.sign_up(
                ClientId=CLIENT_ID,
                SecretHash=get_secret_hash(email),
                Username=email,
                Password=password,
                UserAttributes=[
                    {
                        'Name': "given_name",
                        'Value': given_name
                    },
                    {
                        'Name': "email",
                        'Value': email
                    },
                    {
                        'Name': "custom:custom:company_name",
                        'Value': company_name
                    },
                    {
                        'Name': "custom:custom:tenant_id",
                        'Value': tenant_id
                    },
                    {
                        'Name': "custom:custom:role",
                        'Value': role
                    },
                    {
                        'Name': "custom:custom:account_name",
                        'Value': account_name
                    },

                    {
                        'Name': "custom:title",
                        'Value': title
                    },
                    {
                        'Name': "custom:line_manager",
                        'Value': line_manager
                    },
                    {
                        'Name': "custom:country",
                        'Value': country
                    },
                    {
                        'Name': "custom:address",
                        'Value': address
                    },

                    {
                        'Name': "custom:department",
                        'Value': department
                    },
                    {
                        'Name': "custom:job_title",
                        'Value': job_title
                    },
                    {
                        'Name': "custom:level_twomanager",
                        'Value': level_twomanager
                    },
                    {
                        'Name': "custom:cell_number",
                        'Value': cell_number
                    },
                    {
                        'Name': "custom:date_of_birth",
                        'Value': date_of_birth
                    },
                    {
                        'Name': "custom:start_date",
                        'Value': start_date
                    },
                    {
                        'Name': "custom:town",
                        'Value': town
                    },
                    {
                        'Name': "custom:postcode",
                        'Value': postcode
                    }
                ],

                ValidationData=[
                    {
                        'Name': "email",
                        'Value': email
                    },
                    {
                        'Name': "custom:email",
                        'Value': email
                    }
                ])
            usersub=resp['UserSub']
            return usersub

        except client.exceptions.UsernameExistsException as e:
            return {"error": False,
                    "success": True,
                    "message": "This username already exists",
                    "data": None}
        except client.exceptions.InvalidPasswordException as e:

            return {"error": False,
                    "success": True,
                    "message": "Password should have Caps,\
                                  Special chars, Numbers",
                    "data": None}
        except client.exceptions.UserLambdaValidationException as e:
            return {"error": False,
                    "success": True,
                    "message": "Email already exists",
                    "data": None}

        except Exception as e:
            return {"error": False,
                    "success": True,
                    "message": str(e),
                    "data": None}

        return {"error": False,
                "success": True,
                "message": "Please confirm your signup, \
                                check Email for validation code",
                "data": None}


    given_name = f'{creates.firstname} {creates.lastname}'
    event = {}
    event = {"tenant_id":creates.tenant_id,
             "email": creates.email, "password": creates.password,
             "level_twomanager": creates.level_twomanager,
             "given_name": given_name,
             "company_name": creates.company_name,
             "role": creates.role,
             "account_name": creates.account_name,
             "title": creates.title,
             "country": creates.country,
             "line_manager": creates.line_manager,
             "address": creates.address,
             "department": creates.department,
             "job_title": creates.job_title,
             "cell_number":creates.cell_number,
             "date_of_birth": creates.date_of_birth,
             "start_date": creates.start_date,
             "town": creates.town,
             "postcode": creates.postcode,
             }
    context = "hey"
    get_secret_hash("admintst")
    subid = lambda_handler(event, context)
    print(subid)
    print(type(subid))
    if type(subid) == dict:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is Already Register ")
    else:
        userdata=user.saves(request, subid, db)
        print(userdata)

        return sendmail.usermail(event)
        raise HTTPException(status_code=status.HTTP_201_CREATED, detail="file is uploaded  Sucessfully")




