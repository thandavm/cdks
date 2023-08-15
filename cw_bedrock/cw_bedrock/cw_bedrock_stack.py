from aws_cdk import (
    Duration,
    Stack,
    aws_cloudwatch as cloudwatch
)
from constructs import Construct

class CwBedrockStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define dashboard
        dashboard = cloudwatch.Dashboard(self, "Dashboard")
        dashboard.duration = Duration.days(30)
        
        #Metrics
        invocations = cloudwatch.Metric(    
                namespace="AWS/Bedrock",
                metric_name="Invocations",
                statistic="Sum",
                label="Invocations",
                period= Duration.days(30),
                color=cloudwatch.Color.GREEN                
            )
        input_token_count = cloudwatch.Metric(
                namespace="AWS/Bedrock",
                metric_name="InputTokenCount",
                statistic="Sum",
                label="InputTokenCount",
                period= Duration.days(30),
                color=cloudwatch.Color.GREEN
        )
        output_token_count = cloudwatch.Metric(
                namespace="AWS/Bedrock",
                metric_name="OutputTokenCount",
                statistic="Sum",
                label="OutputTokenCount",
                period= Duration.days(30),
                color=cloudwatch.Color.GREEN
                )
        
        # Add widget to dashboard
        dashboard.add_widgets(cloudwatch.SingleValueWidget(
            metrics= [invocations, input_token_count, output_token_count]))
