from  django.conf import settings
import requests

class Paystack:
    PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET
    base_url = 'https://api.paystack.co'
    
    def verify_within(self, ref , amount, *args, **kwargs):
        path=(f"/transaction/verify/{ref}")
        
        headers = {
            "Authorization": f"Bearer {self.PAYSTACK_SECRET_KEY}",
            "content-type": "application/json",
        } 
        url = self.base_url + path
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            res_data = res.json()
            status = res_data['status']
            result = res_data['data']
            return status, result
        return res_data['status'], res_data['message']
        
            
        
        