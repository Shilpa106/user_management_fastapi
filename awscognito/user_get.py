import boto3
from fastapi import status,HTTPException
aws_region = 'eu-west-1'
userpool_id = 'eu-west-1_vZqAAJiUV'
aws_access_key="AKIA55EX7HXTVQNPB25D"


aws_secret_key="ehH/h9DXF0hoSxilcUYmCGRn3BHNlb8KNXiwNE9Q"
def handler(id, creates):
    print(creates)
    print("fdfdfdfd",id)

    def lambda_handler(event, context):
        for field in ["given_name", "company_name", "tenant_id", "role", "account_name", "title",
                      "country",
                      "line_manager", "address", "department", "job_title", "cell_number", "level_twomanager",
                      "date_of_birth", "start_date"
                                       "town", "postcode"]:
            # print(field)
            pass

        given_name = event['given_name']
        company_name = event['company_name']
        tenant_id = event['tenant_id']
        role = event['role']
        account_name = event['account_name']
        title = event['title']
        country = event['country']
        line_manager = event['line_manager']
        address = event['address']
        department = event['department']
        job_title = event['job_title']
        level_twomanager = event['level_twomanager']
        cell_number = event['cell_number']
        date_of_birth = event['date_of_birth']
        start_date = event['start_date']
        town = event['town']
        postcode = event['postcode']

        client = boto3.client('cognito-idp',
                              region_name=aws_region,
                              aws_access_key_id=aws_access_key,
                              aws_secret_access_key=aws_secret_key)
        try:
            response = client.admin_update_user_attributes(
                UserPoolId=userpool_id,
                Username=id,

                UserAttributes=[
                    {
                        'Name': "given_name",
                        'Value': given_name
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
            )
            print("dsfdsfdsfds", response)

        except client.exceptions.InvalidParameterException as e:
            return {"error": True,
                    "success": False,
                    "data": None,
                    "message": "InvalidParameterException"}

        except client.exceptions.ResourceNotFoundException as e:
            return {"error": True,
                    "success": False,
                    "data": None,
                    "message": "ResourceNotFoundException "}

        except client.exceptions.TooManyRequestsException as e:
            return {"error": True,
                    "success": False,
                    "data": None,
                    "message": "TooManyRequestsException "}

        except client.exceptions.NotAuthorizedExceptionas as e:

            return {"error": True,
                    "success": False,
                    "data": None,
                    "message": "User NotAuthorized Exceptionas "}

        except client.exceptions.InternalErrorException as e:
            return {"error": True,
                    "success": False,
                    "data": None,
                    "message": "InternalErrorException "}

        except client.exceptions.UserNotFoundException as e:
            return {"error": True,
                    "success": False,
                    "data": None,
                    "message": "UserNotFoundException "}

        except Exception as e:
            return {"error": False,
                    "success": True,
                    "message": str(e),
                    "data": None}

    given_name = f'{creates.firstname} {creates.lastname}'
    event = {}
    event = {"tenant_id": creates.tenant_id,
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
             "cell_number": creates.cell_number,
             "date_of_birth": creates.date_of_birth,
             "start_date": creates.start_date,
             "town": creates.town,
             "postcode": creates.postcode,
             }
    context = "hey"
    lambda_handler(event, context)
    raise HTTPException(status_code=status.HTTP_201_CREATED, detail="User is Updated Sucessfully ")
