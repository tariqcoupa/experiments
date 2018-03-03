#!/usr/bin/python 
import SoftLayer
import pprint

class bandwidth():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self):
        pp = pprint.PrettyPrinter(indent=2)
        theMask = "mask[inboundPrivateBandwidthUsage,inboundPublicBandwidthUsage,outboundPrivateBandwidthUsage,outboundPublicBandwidthUsage]"
        result = self.client['SoftLayer_Account'].getHardware()
        print "server_name,public_in,public_out,private_in,private_out,AllocatedBandWidth"
        
        for server in result:
            #getHardware() only returns SoftLayer_Hardware, which doesn't have the private bw usage metrics, for some reason.
            # So we just use SoftLayer_Hardware_Server here, which has more detailed information
            serverInfo = self.client['SoftLayer_Hardware_Server'].getObject(id=server['id'],mask=theMask)
	    #alloc_info = self.client['Softlayer_Hardware_Server'].getDatacenter(id=server['id'])	

            # use .get() to avoid exceptions
            pubin = serverInfo.get('inboundPublicBandwidthUsage', '--')
            pubout = serverInfo.get('outboundPublicBandwidthUsage', '--')
            privin =serverInfo.get('inboundPrivateBandwidthUsage', '--')
            privout = serverInfo.get('outboundPrivateBandwidthUsage', '--')

            print(serverInfo['fullyQualifiedDomainName'] + ","),
            print(pubin + ","),
            print(pubout + ","),
            print(privin + ","),
            print(privout)
	    #print(alloc_info)
	

if __name__ == "__main__":
    main = bandwidth()
    main.main()
