"""
CoverBridge V2 API Gateway
Orchestration Layer Entrypoint
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI(
    title="CoverBridge V2 - AI Platform",
    description="Enterprise API Gateway orchestrating AI Agents and Core Services",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ArchitectureLayer(BaseModel):
    name: str
    description: str
    components: List[str]


@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "operational", "version": "2.0.0"}


@app.get("/api/system/architecture", response_model=List[ArchitectureLayer], tags=["System"])
async def get_system_architecture():
    """
    Dynamically returns the true underlying architecture of the V2 Backend platform.
    The frontend can use this to render the 7-Layer Architecture visualization.
    """
    return [
        {
            "name": "Experience Layer",
            "description": "Multi-channel user interfaces",
            "components": ["Customer Portal", "Broker Dashboard", "Admin Console", "WhatsApp/Mobile"]
        },
        {
            "name": "Orchestration Layer",
            "description": "API Gateway and Workflow Management",
            "components": ["API Gateway", "Event Bus", "Workflow Engine", "Identity/IAM"]
        },
        {
            "name": "Agentic AI Layer",
            "description": "Autonomous specialized agents",
            "components": ["Underwriting Agent", "Claim Agent", "Support Agent", "Fraud Agent"]
        },
        {
            "name": "Core Services Layer",
            "description": "Fundamental insurance operations",
            "components": ["Policy Admin", "Billing", "Document Gen", "Claims Mgmt"]
        },
        {
            "name": "AI Factory Layer",
            "description": "Machine Learning infrastructure",
            "components": ["Model Registry", "Vector DB", "Training Pipeline", "Prompt Mgmt"]
        },
        {
            "name": "Data Layer",
            "description": "Data storage and synchronization",
            "components": ["Data Lake", "Operational DB", "Analytics Warehouse", "IRDAI Sync"]
        },
        {
            "name": "Foundation Layer",
            "description": "Cloud infrastructure and security",
            "components": ["Kubernetes", "Monitoring/APM", "CI/CD", "Security"]
        }
    ]

# TODO: Include routers from agents, core, ai_factory, data modules
