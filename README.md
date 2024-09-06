# Enable-Disable-EventBridge-Rule-LambdaxEventBridge-
start/stop event bridge schedule by using lamdba and event bridge in AWS

### Steps:

1. **Create Lambda Function**: This Lambda will manage the EventBridge rule state.
2. **Trigger Lambda with EventBridge**: You can use EventBridge to trigger this Lambda and pass variables (e.g., `enable` or `disable`).

### How It Works:

- **Input Event**: The `event` will contain:
    - `rule_name`: Name of the EventBridge rule to be managed.
    - `action`: Either `'enable'` or `'disable'`, determining what action to take.
- **Lambda Execution**: The Lambda checks the action and enables/disables the EventBridge rule accordingly.

### Setting Up the EventBridge Rule to Trigger Lambda:

1. **Create the EventBridge Rule**:
    - Go to AWS EventBridge, create a new rule, and set the trigger to execute your Lambda function.
2. **Add EventBridge Trigger**:
    - In the rule's configuration, add the Lambda function you've created.
    - You can use EventBridge to trigger the Lambda function based on various events (like a schedule or specific events from other AWS services).
3. **Pass Variables**:
    - Ensure that the input event to the Lambda includes the `rule_name` and `action` fields. You can pass these dynamically based on your EventBridge event pattern.

With this setup, you can manage the state of an EventBridge rule using Lambda, and trigger it based on an EventBridge schedule or specific events.