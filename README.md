<h1>COWIN API</h1>

During these challenging times, keeping track of vaccine availibility is another headache.So I've made this python script which gets the details of all the vaccination centers every n second ( can be modified from code ) from the COWIN API Portal and it can send you an android notification or a whatsaap message when a slot opens up!

For sendig Android notifications, I am using notify_run python module and for sending whatsaap message I am using Twilio whatsaap API.
Both these modules need some initial registration and setup which can be found in the module's documentation.
