import boto3
import json
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def lambda_handler(event, context):
    """
    Lambda function to enable or disable an EventBridge rule.
    
    :param event: The input event, which should contain the rule_name and action ('enable' or 'disable')
    :param context: The Lambda context object (not used here)
    """
    client = boto3.client('events')
    
    # Get the rule name and action from the event
    rule_name = event.get('rule_name', '')
    action = event.get('action', '').lower()  # Either 'enable' or 'disable'
    
    if not rule_name:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: rule_name is required.')
        }

    if action not in ['enable', 'disable']:
        return {
            'statusCode': 400,
            'body': json.dumps("Error: action must be either 'enable' or 'disable'.")
        }

    try:
        if action == 'enable':
            client.enable_rule(Name=rule_name)
            return {
                'statusCode': 200,
                'body': json.dumps(f"Rule '{rule_name}' has been enabled.")
            }
        elif action == 'disable':
            client.disable_rule(Name=rule_name)
            return {
                'statusCode': 200,
                'body': json.dumps(f"Rule '{rule_name}' has been disabled.")
            }
    
    except NoCredentialsError:
        return {
            'statusCode': 500,
            'body': json.dumps('Error: AWS credentials not found.')
        }
    except PartialCredentialsError:
        return {
            'statusCode': 500,
            'body': json.dumps('Error: Incomplete AWS credentials.')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }

