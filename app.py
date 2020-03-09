#!/usr/bin/env python3

from aws_cdk import core

from cdksample.network_stack import NetworkStack
from cdksample.network_dr_stack import NetworkDRStack
from cdksample.bastion_stack import BastionStack
from cdksample.bastion_dr_stack import BastionDRStack
from cdksample.resource_domain_stack import ResourceDomainStack
from cdksample.resource_domain_dr_stack import ResourceDomainDRStack
from cdksample.japan_domain_stack import JapanDomainStack

app = core.App()
prefix = app.node.try_get_context('stack_prefix')
env = core.Environment(
    account=app.node.try_get_context('account'),
    region='ap-northeast-1'
)
env_dr = core.Environment(
    account=app.node.try_get_context('account'),
    region='ap-northeast-2'
)
props = dict()

network_stack = NetworkStack(app, '{}-NetworkStack'.format(prefix), env=env, props=props)
props = network_stack.outputs

network_dr_stack = NetworkDRStack(app, '{}-NetworkDRStack'.format(prefix), env=env_dr, props=props)
props = network_dr_stack.outputs

bastion_stack = BastionStack(app, '{}-BastionStack'.format(prefix), env=env, props=props)
props = bastion_stack.outputs

bastion_dr_stack = BastionDRStack(app, '{}-BastionDRStack'.format(prefix), env=env_dr, props=props)
props = bastion_dr_stack.outputs

resource_domain_stack = ResourceDomainStack(app, '{}-ResourceDomainStack'.format(prefix), env=env, props=props)
props = resource_domain_stack.outputs

resource_domain_dr_stack = ResourceDomainDRStack(app, '{}-ResourceDomainDRStack'.format(prefix), env=env_dr, props=props)
props = resource_domain_dr_stack.outputs

japan_domain_stack = JapanDomainStack(app, '{}-JapanDomainStack'.format(prefix), env=env, props=props)
props = japan_domain_stack.outputs

app.synth()
