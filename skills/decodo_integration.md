---
name: decodo-api
description: Integration with Decodo proxy provider
---

# Decodo API Integration

Purpose:
Automatically provision proxies from Decodo.

Workflow:

user buys proxy
↓
create order
↓
call Decodo API
↓
create proxy
↓
store proxy in database
↓
assign to user

Features:

• automatic provisioning
• proxy pool sync
• geo proxy support