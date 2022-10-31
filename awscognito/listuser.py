import boto3
from fastapi import status,HTTPException
aws_region = 'eu-west-1'
userpool_id = 'eu-west-1_vZqAAJiUV'
aws_access_key="AKIA55EX7HXTVQNPB25D"


aws_secret_key="ehH/h9DXF0hoSxilcUYmCGRn3BHNlb8KNXiwNE9Q"




def list_user():
    client = boto3.client('cognito-idp',
                          region_name=aws_region,
                          aws_access_key_id=aws_access_key,
                          aws_secret_access_key=aws_secret_key)
    try:

        response = client.list_users(
            UserPoolId=userpool_id,
        )
        return response

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

    except Exception as e:
        return {"error": False,
                "success": True,
                "message": str(e),
                "data": None}













