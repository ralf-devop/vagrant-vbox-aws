#!/usr/bin/env python3

import aws_cdk as cdk

from who_needs_a_server_anyway.who_needs_a_server_anyway_stack import WhoNeedsAServerAnywayStack


app = cdk.App()
WhoNeedsAServerAnywayStack(app, "WhoNeedsAServerAnywayStack")

app.synth()
