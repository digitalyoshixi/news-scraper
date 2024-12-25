from ollama import chat
from ollama import ChatResponse

def getresp(message : str):
    response: ChatResponse = chat(model='llama3.1', messages=[
      {
        'role': 'user',
        'content': f"Respond only with a concise 4 sentence summary of the following article. Do not include a concluding sentence. {message}"
      },
    ])
    # or access fields directly from the response object
    return str(response.message.content)




'''
print(getresp(
        """
Over five months after publicly scrapping the first version of the Windows Recall feature for its first wave of Copilot+ PCs, Microsoft announced today that a newly rearchitected version of Recall is finally ready for public consumption.

For now, the preview will be limited to a tiny subset of PCs: Qualcomm Snapdragon X Elite and Plus Copilot+ PCs enrolled in the Dev channel of the Windows Insider program (the build of Windows that includes Recall is 26120.2415). Intel and AMD Copilot+ PCs can’t access the Recall preview yet, and regular Windows 11 PCs won’t support the feature at all.

If you haven’t been following along, Recall is one of Microsoft’s many AI-driven Windows features exclusive to Copilot+ PCs, which come with a built-in neural processing unit (NPU) capable of running AI and machine learning workloads locally on your device rather than in the cloud. When enabled, Recall runs in the background constantly, taking screenshots of all your activity and saving both the screenshots and OCR’d text to a searchable database so that users can retrace their steps later.

The initial version of Recall never officially launched, but testers (including Ars) managed to enable it on unsupported PCs in a Windows Insider build. Recall originally stored all of the screenshots and text on disk in plaintext with no additional encryption or any other protections, and users with local or remote access to the machine could easily copy and open other users’ Recall data. Since the feature was opt-out by default and took no steps to hide sensitive information (users could exclude certain sites or apps from being saved by Recall, but that had to be done entirely manually), security researchers and other users correctly identified it as a huge security and privacy risk.
Users will be asked to reauthenticate with Windows Hello every time they access their Recall database. Credit: Microsoft

Microsoft has now delayed the feature multiple times to address those concerns, and it outlined multiple security-focused additions to Recall in a blog post in September. Among other changes, the feature is now opt-in by default and is protected by additional encryption. Users must also re-authenticate with Windows Hello each time they access the database. Turning on the feature requires Secure Boot, BitLocker disk encryption, and Windows Hello to be enabled. In addition to the manual exclusion lists for sites and apps, the new Recall also attempts to mask sensitive data like passwords and credit card numbers so they aren't stored in the Recall database.

The new version of Recall can also be completely uninstalled for users who have no interest in it, or by IT administrators who don't want to risk it exposing sensitive data.

Testers will need to kick the tires on all of these changes to make sure that they meaningfully address all the risks and issues that the original version of Recall had, and this Windows Insider preview is their chance to do it.
“Do security”

Part of the original Recall controversy was that Microsoft wasn’t going to run it through the usual Windows Insider process—it was intended to be launched directly to users of the new Copilot+ PCs via a day-one software update. This in itself was a big red flag; usually, even features as small as spellcheck for the Notepad app go through multiple weeks of Windows Insider testing before Microsoft releases them to the public. This gives the company a chance to fix bugs, collect and address user feedback, and even scrub new features altogether.

Microsoft is supposedly re-orienting itself to put security over all other initiatives and features. CEO Satya Nadella recently urged employees to “do security” when presented with the option to either launch something quickly or launch something securely. In Recall’s case, the company’s rush to embrace generative AI features almost won out over that “do security” mandate. If future AI features go through the typical Windows Insider testing process first, that will be a sign that Microsoft is taking its commitment to security seriously.
"""
))
'''