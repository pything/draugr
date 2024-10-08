#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 19/03/2020
           """

HOST = "127.0.0.1:7233"  # Go Echo UI @ 8233
NAMESPACE = (
    "default"  # use 'default' for now, must first create a 'mi_integration' namespace
)

IGNORE = """
    WorkflowServiceStubs service =
        WorkflowServiceStubs.newInstance(
            WorkflowServiceStubsOptions.newBuilder().setTarget(serviceAddress).build());
    RegisterNamespaceRequest request =
        RegisterNamespaceRequest.newBuilder()
            .setName(NAMESPACE)
            .setWorkflowExecutionRetentionPeriod(Durations.fromDays(7))
            .build();
    service.blockingStub().registerNamespace(request);

"""
