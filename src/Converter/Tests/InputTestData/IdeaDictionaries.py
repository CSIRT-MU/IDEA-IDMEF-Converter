

def get_dict1():
    return {
        "Format": "IDEA0",
        "ID": "2E4A3926-B1B9-41E3-89AE-B6B474EB0A54",
        "AltNames": ["altname1", "altname2"],
        "CorrelID": ["3E4A3926-B1B9-41E3-89AE-B6B474EB0A56", "4E4A3926-B1B9-41E3-89AE-B6B474EB0A57",
                     "5E4A3926-B1B9-41E3-89AE-B6B474EB0A58"],
        "AggrID": ["6E4A3926-B1B9-41E3-89AE-B6B474EB0A57", "6E4A3926-B1B9-41E3-89AE-B6B474EB0A58",
                   "6E4A3926-B1B9-41E3-89AE-B6B474EB0A59"],
        "PredID": ["6E4A7777-B1B9-41E3-89AE-B6B474EB0A57", "6E4A7777-B1B9-41E3-89AE-B6B474EB0A58",
                   "6E4A7777-B2B9-41E3-89AE-B6B474EB0A59"],
        "RelID": ["6E4A7777-B1B9-41E3-89AE-B6B474EB0A22", "6E4A7777-B1B9-41E3-89AE-B6B474EB0A11",
                  "6E4A7777-B2B9-41E3-89AE-B6B474EB0A33"],
        "CreateTime": "2017-03-23T10:10:42Z",
        "DetectTime": "2017-03-23T09:15:50Z",
        "EventTime": "2017-03-22T21:12:05Z",
        "CeaseTime": "2017-02-22T21:11:05Z",
        "WinStartTime": "2017-02-22T21:12:10Z",
        "WinEndTime": "2017-02-22T21:14:38Z",
        "ConnCount": 3,
        "FlowCount": 4,
        "PacketCount": 248,
        "ByteCount": 720468,
        "Category": ["Abusive.Spam", "Fraud.Phishing"],
        "Ref": ["http://www.example.com", "http://www.other.example.com"],
        "Confidence": 0.563,
        "Description": "Test message for converter",
        "Note": "No field of this message is real",
        "Source":
            [
                {
                    "Type": ["OriginSpam", "Phishing"],
                    "Hostname": ["hostexample.com", "nameexample.com"],
                    "IP4": ["93.184.216.119"],
                    "IP6": ["2001:db8::2:1", "2001:db8:a::123/64"],
                    "MAC": ["01:23:45:67:89:ab", "01:23:45:67:89:cd"],
                    "Email": ["example@example.com", "example2@example2.com"],
                    "Proto": ["tcp2", "epmap2"],
                    "Port": [245],
                    "URL": ["http://www.sourceexample.com", "http://www.source.otherexample.com"],
                    "Spoofed": False,
                    "AttachHand": ["abc1", "abc2"],
                    "Note": "First test source",
                    "Imprecise": True,
                    "Anonymised": False,
                    "ASN": [15, 231],
                    "Router": ["router1", "router2"],
                    "Netname": ["example:EXAMPLE", "example2:EXAMPLE2"],
                    "Ref": ["sourceref.example.com", "sorceref.other.example.com"]
                },
                {
                    "Type": ["Phishing"],
                    "Hostname": ["hostexample2.com", "othernameexample.com"],
                    "IP4": ["93.184.216.119", "93.184.216.120"],
                    "IP6": ["2001:db8::2:1", "2001:db8:a::123/64"],
                    "MAC": ["01:23:45:67:89:ab", "01:23:45:67:89:cd"],
                    "Email": ["example@example.com", "example2@example2.com"],
                    "Proto": ["tcp2", "epmap2"],
                    "Port": [210, 542],
                    "URL": ["http://www.sourceexample.com", "http://www.source.otherexample.com"],
                    "Spoofed": False,
                    "AttachHand": ["def", "def2"],
                    "Note": "Second test source",
                    "Imprecise": True,
                    "Anonymised": False,
                    "ASN": [15, 231],
                    "Router": ["router1", "router2"],
                    "Netname": ["example:EXAMPLE", "example2:EXAMPLE2"],
                    "Ref": ["sourceref.example.com", "sorceref.other.example.com"]
                }
            ],
        "Target":
            [
                {
                    "Type": ["Open"],
                    "Hostname": ["targethostexample.com", "targetnameexample.com"],
                    "IP4": ["0.184.216.119"],
                    "IP6": ["0:db8::2:1", "2001:db8:a::123/64"],
                    "MAC": ["00:00:45:67:89:ab", "00:23:45:67:89:ed"],
                    "Email": ["example00@example.com", "example000@example2.com"],
                    "Proto": ["tcp", "epmap"],
                    "Port": [80],
                    "URL": ["http://www.targetexample.com", "http://www.target.otherexample.com"],
                    "Spoofed": True,
                    "AttachHand": ["att1", "att2"],
                    "Note": "First test target",
                    "Imprecise": True,
                    "Anonymised": False,
                    "ASN": [15, 231],
                    "Router": ["router3", "router4"],
                    "Netname": ["example:EXAMPLE", "example2:EXAMPLE2"],
                    "Ref": ["tar.example.com", "other.example.com"]
                },
                {
                    "Type": ["Open"],
                    "Hostname": ["example.com", "othertarget.com"],
                    "IP4": ["0.0.216.119"],
                    "IP6": ["0:0::2:1", "00:db8:a::123/64"],
                    "MAC": ["00:00:00:67:89:ab", "00:23:45:67:89:fd"],
                    "Email": ["example00@example.com", "example000@example2.com"],
                    "Proto": ["tcp2", "epmap2"],
                    "Port": [210, 542],
                    "URL": ["http://www.targetxmpl.com", "http://www.target.otherexample.com"],
                    "Spoofed": False,
                    "AttachHand": ["att3", "att4"],
                    "Note": "Second test target",
                    "Imprecise": True,
                    "Anonymised": True,
                    "ASN": [15, 231],
                    "Router": ["router5", "router6"],
                    "Netname": ["example:EXAMPLE", "example2:EXAMPLE2"],
                    "Ref": ["target.example.com", "ref.other.example.com"]
                }
            ],
        "Attach":
            [
                {
                    "Handle": "att1",
                    "FileName": ["file1.txt", "file2"],
                    "Type": ["Malware"],
                    "Hash": ["sha1:794467071687f7c59d033f4de5ece6b46415b633",
                             "md5:dc89f0b4ff9bd3b061dd66bb66c991b1"],
                    "Size": 200,
                    "Ref": ["example.com", "other.example.com"],
                    "Note": "First test attach",
                    "ContentType": ["mediatype"],
                    "ContentCharset": "UTF-8",
                    "ContentEncoding": "base64",
                    "Content": "This is content of the attach",
                    "ContentID": ["1", "2"],
                    "ExternalURI": ["external.example.com"]
                },
                {
                    "Handle": "att2",
                    "FileName": ["file1.txt", "file2"],
                    "Type": ["Malware"],
                    "Hash": ["sha1:794467071687f7c59d033f4de5ece6b46415b604",
                             "md5:dc89f0b4ff9bd3b061dd66bb66c99100"],
                    "Size": 300,
                    "Ref": ["example.com", "other.example.com"],
                    "Note": "First test attach",
                    "ContentType": ["mediatype"],
                    "ContentCharset": "UTF-8",
                    "ContentEncoding": "base64",
                    "Content": "This is content of the attach",
                    "ContentID": ["1", "2"],
                    "ExternalURI": ["external.example.com"]
                },
                {
                    "Handle": "att3",
                    "FileName": ["file1.txt", "file2"],
                    "Type": ["Malware"],
                    "Hash": ["sha1:794467071687f7c59d033f4de5ece6b46415b601",
                             "md5:dc89f0b4ff9bd3b061dd66bb66c99102"],
                    "Size": 400,
                    "Ref": ["example.com", "other.example.com"],
                    "Note": "Second test attach",
                    "ContentType": ["mediatype"],
                    "ContentCharset": "UTF-8",
                    "ContentEncoding": "base64",
                    "Content": "This is content of the attach",
                    "ContentID": ["1", "2"],
                    "ExternalURI": ["external.example.com"]
                }
            ],
        "Node":
            [
                {
                    "Name": "com.example.specific",
                    "Type": ["Log", "Statistical"],
                    "SW": ["Example software", "Example software 2"],
                    "AggrWin": "536D10:20:30.5",
                    "Note": "First test node"
                },
                {
                    "Name": "com.example.node",
                    "Type": ["Log", "Statistical"],
                    "SW": ["Example software"],
                    "AggrWin": "425D10:20:35.1",
                    "Note": "Second test node"
                }
            ]
    }


def get_expected_dict2():
    return {
        "Format": "IDEA0",
        "ID": "1E4A3926-B1B9-41E3-89AE-B6B474EB0A54",
        "AltNames": ["altname8", "altname9"],
        "CorrelID": ["3E4A3925-B1B9-41E3-89AE-B6B474EB0A56", "4E4A3926-B1B9-41E3-89AE-B6B474EBBA57",
                     "5E4A3926-B1B9-41E3-89AE-B6B474EB0A41"],
        "AggrID": ["6E4A3926-B1B9-41E3-89AE-B6B474EB0A57", "6E4A3926-B1B9-41E3-89AE-B6B474EB0A58",
                   "6E4A3926-B1B9-41E3-89AE-B6B474EB0A65"],
        "PredID": ["6E4A7777-B1B9-41E3-89AE-B6B474EB0A57", "6E4A7777-B1B9-41E3-89AE-B6B474EB0A58",
                   "6E4A7777-B2B9-41E3-89AE-B6B474EB0A59"],
        "RelID": ["6E4A7777-B1B9-41E3-89AE-B6B474EB0A22", "6E4A7777-B1B9-41E3-89AE-B6B474EB0A11",
                  "6E4A7777-B2B9-41E3-89AE-B6B474EB0A33"],
        "CreateTime": "2016-03-23T10:10:42Z",
        "DetectTime": "2015-03-23T09:15:50Z",
        "EventTime": "2014-03-22T21:12:05Z",
        "CeaseTime": "2013-02-22T21:11:05Z",
        "WinStartTime": "2012-02-22T21:12:10Z",
        "WinEndTime": "2011-02-22T21:14:38Z",
        "ConnCount": 5,
        "FlowCount": 9,
        "PacketCount": 248,
        "ByteCount": 220468,
        "Category": ["Abusive.Spam", "Fraud.Phishing"],
        "Ref": ["http://www.example.com", "http://www.other.example.com"],
        "Confidence": 0.563,
        "Description": "Test message for converter",
        "Note": "No field of this message is real",
        "Source":
            [
                {
                    "Type": ["OriginSpam", "Phishing"],
                    "Hostname": ["hostexample.com", "nameexample.com"],
                    "IP4": ["112.184.216.119"],
                    "IP6": ["2001:db8::2:1", "2001:db8:a::123/64"],
                    "MAC": ["01:23:45:67:89:ab", "01:23:45:67:89:cd"],
                    "Email": ["example@example.com", "example2@example2.com"],
                    "Proto": ["tcp2", "epmap2"],
                    "Port": [245],
                    "URL": ["http://www.sourceexample.com", "http://www.source.otherexample.com"],
                    "Spoofed": True,
                    "AttachHand": ["abc1", "abc2"],
                    "Note": "First test source",
                    "Imprecise": True,
                    "Anonymised": False,
                    "ASN": [15, 231],
                    "Router": ["router1", "router2"],
                    "Netname": ["example:EXAMPLE", "example2:EXAMPLE2"],
                    "Ref": ["sourceref.example.com", "sorceref.other.example.com"]
                },
                {
                    "Type": ["Phishing"],
                    "Hostname": ["hostexample2.com", "othernameexample.com"],
                    "IP4": ["93.184.216.119", "93.184.216.120"],
                    "IP6": ["2001:db8::2:1", "2001:db8:a::123/64"],
                    "MAC": ["01:23:45:67:89:ab", "01:23:45:67:89:cd"],
                    "Email": ["example@example.com", "example2@example2.com"],
                    "Proto": ["tcp2", "epmap2"],
                    "Port": [210, 542],
                    "URL": ["http://www.sourceexample.com", "http://www.source.otherexample.com"],
                    "Spoofed": False,
                    "AttachHand": ["def", "def2"],
                    "Note": "Second test source",
                    "Imprecise": True,
                    "Anonymised": False,
                    "ASN": [15, 231],
                    "Router": ["router1", "router2"],
                    "Netname": ["example:EXAMPLE", "example2:EXAMPLE2"],
                    "Ref": ["sourceref.example.com", "sorceref.other.example.com"]
                }
            ],
        "Target":
            [
                {
                    "Type": ["Open"],
                    "Hostname": ["targethostexample.com", "targetnameexample.com"],
                    "IP4": ["0.184.216.119"],
                    "IP6": ["0:db8::2:1", "2001:db8:a::123/64"],
                    "MAC": ["00:00:45:67:89:ab", "00:23:45:67:89:ed"],
                    "Email": ["example00@example.com", "example000@example2.com"],
                    "Proto": ["tcp", "epmap"],
                    "Port": [80],
                    "URL": ["http://www.targetexample.com", "http://www.target.otherexample.com"],
                    "Spoofed": True,
                    "AttachHand": ["att1", "att2"],
                    "Note": "First test target",
                    "Imprecise": True,
                    "Anonymised": False,
                    "ASN": [35, 231],
                    "Router": ["router3", "router4"],
                    "Netname": ["example:EXAMPLE", "example2:EXAMPLE2"],
                    "Ref": ["tar.example.com", "other.example.com"]
                },
                {
                    "Type": ["Open"],
                    "Hostname": ["example.com", "othertarget.com"],
                    "IP4": ["0.0.216.119"],
                    "IP6": ["0:0::2:1", "00:db8:a::123/64"],
                    "MAC": ["00:00:00:67:89:ab", "00:23:45:67:89:fd"],
                    "Email": ["example00@example.com", "example000@example2.com"],
                    "Proto": ["tcp2", "epmap2"],
                    "Port": [210, 542],
                    "URL": ["http://www.targetxmpl.com", "http://www.target.otherexample.com"],
                    "Spoofed": False,
                    "AttachHand": ["att3", "att4"],
                    "Note": "Second test target",
                    "Imprecise": True,
                    "Anonymised": True,
                    "ASN": [15, 231],
                    "Router": ["router5", "router6"],
                    "Netname": ["example:EXAMPLE", "example2:EXAMPLE2"],
                    "Ref": ["target.example.com", "ref.other.example.com"]
                }
            ],
        "Attach":
            [
                {
                    "Handle": "att1",
                    "FileName": ["file1.txt", "file2"],
                    "Type": ["Malware"],
                    "Hash": ["sha1:794467071687f7c59d033f4de5ece6b46415b633",
                             "md5:dc89f0b4ff9bd3b061dd66bb66c991b1"],
                    "Size": 200,
                    "Ref": ["other.example.com"],
                    "Note": "First test attach",
                    "ContentType": ["mediatype"],
                    "ContentCharset": "UTF-8",
                    "ContentEncoding": "base64",
                    "Content": "This is content of the attach",
                    "ContentID": ["1", "2"],
                    "ExternalURI": ["external.example.com"]
                },
                {
                    "Handle": "att2",
                    "FileName": ["file1.txt", "file2"],
                    "Type": ["Malware"],
                    "Hash": ["sha1:794467071687f7c59d033f4de5ece6b46415b604",
                             "md5:dc89f0b4ff9bd3b061dd66bb66c99100"],
                    "Size": 300,
                    "Ref": ["example.com", "other.example.com"],
                    "Note": "First test attach",
                    "ContentType": ["mediatype"],
                    "ContentCharset": "UTF-8",
                    "ContentEncoding": "base64",
                    "Content": "This is content of the attach",
                    "ContentID": ["1", "2"],
                    "ExternalURI": ["external.example.com"]
                },
                {
                    "Handle": "att3",
                    "FileName": ["file1.txt", "file2"],
                    "Type": ["Malware"],
                    "Hash": ["sha1:794467071687f7c59d033f4de5ece6b46415b601",
                             "md5:dc89f0b4ff9bd3b061dd66bb66c99102"],
                    "Size": 400,
                    "Ref": ["example.com", "other.example.com"],
                    "Note": "Second test attach",
                    "ContentType": ["mediatype"],
                    "ContentCharset": "UTF-8",
                    "ContentEncoding": "base64",
                    "Content": "This is content of the attach",
                    "ContentID": ["1", "2"],
                    "ExternalURI": ["external.example.com"]
                }
            ],
        "Node":
            [
                {
                    "Name": "com.example.specific",
                    "Type": ["Log", "Statistical"],
                    "SW": ["Example software", "Example software 2"],
                    "AggrWin": "536D10:20:30.5",
                    "Note": "First test node"
                },
                {
                    "Name": "com.example.node",
                    "Type": ["Log", "Statistical"],
                    "SW": ["Example software"],
                    "AggrWin": "425D10:20:35.2",
                    "Note": "Second test node"
                }
            ]
    }


def get_test_string():
    return """{
        "Format": "IDEA0",
        "ID": "2E4A3926-B1B9-41E3-89AE-B6B474EB0A54",
        "AltNames": ["altname1", "altname2"],
        "CorrelID": ["3E4A3926-B1B9-41E3-89AE-B6B474EB0A56", "4E4A3926-B1B9-41E3-89AE-B6B474EB0A57",
                     "5E4A3926-B1B9-41E3-89AE-B6B474EB0A58"],
        "AggrID": ["6E4A3926-B1B9-41E3-89AE-B6B474EB0A57", "6E4A3926-B1B9-41E3-89AE-B6B474EB0A58",
                   "6E4A3926-B1B9-41E3-89AE-B6B474EB0A59"],
        "PredID": ["6E4A7777-B1B9-41E3-89AE-B6B474EB0A57", "6E4A7777-B1B9-41E3-89AE-B6B474EB0A58",
                   "6E4A7777-B2B9-41E3-89AE-B6B474EB0A59"],
        "RelID": ["6E4A7777-B1B9-41E3-89AE-B6B474EB0A22", "6E4A7777-B1B9-41E3-89AE-B6B474EB0A11",
                  "6E4A7777-B2B9-41E3-89AE-B6B474EB0A33"],
        "CreateTime": "2017-03-23T10:10:42Z",
        "DetectTime": "2017-03-23T09:15:50Z",
        "EventTime": "2017-03-22T21:12:05Z",
        "CeaseTime": "2017-02-22T21:11:05Z",
        "WinStartTime": "2017-02-22T21:12:10Z",
        "WinEndTime": "2017-02-22T21:14:38Z",
        "ConnCount": 3,
        "FlowCount": 4,
        "PacketCount": 248,
        "ByteCount": 720468,
        "Category": ["Abusive.Spam", "Fraud.Phishing"],
        "Ref": ["http://www.example.com", "http://www.other.example.com"],
        "Confidence": 0.563,
        "Description": "Test message for converter",
        "Note": "No field of this message is real",
        "Source":
            [
                {
                    "Type": ["OriginSpam", "Phishing"],
                    "Hostname": ["hostexample.com", "nameexample.com"],
                    "IP4": ["93.184.216.119"],
                    "IP6": ["2001:db8::2:1", "2001:db8:a::123/64"],
                    "MAC": ["01:23:45:67:89:ab", "01:23:45:67:89:cd"],
                    "Email": ["example@example.com", "example2@example2.com"],
                    "Proto": ["tcp2", "epmap2"],
                    "Port": [245],
                    "URL": ["http://www.sourceexample.com", "http://www.source.otherexample.com"],
                    "Spoofed": false,
                    "AttachHand": ["abc1", "abc2"],
                    "Note": "First test source",
                    "Imprecise": true,
                    "Anonymised": false,
                    "ASN": [15, 231],
                    "Router": ["router1", "router2"],
                    "Netname": ["example:EXAMPLE", "example2:EXAMPLE2"],
                    "Ref": ["sourceref.example.com", "sorceref.other.example.com"]
                },
                {
                    "Type": ["Phishing"],
                    "Hostname": ["hostexample2.com", "othernameexample.com"],
                    "IP4": ["93.184.216.119", "93.184.216.120"],
                    "IP6": ["2001:db8::2:1", "2001:db8:a::123/64"],
                    "MAC": ["01:23:45:67:89:ab", "01:23:45:67:89:cd"],
                    "Email": ["example@example.com", "example2@example2.com"],
                    "Proto": ["tcp2", "epmap2"],
                    "Port": [210, 542],
                    "URL": ["http://www.sourceexample.com", "http://www.source.otherexample.com"],
                    "Spoofed": false,
                    "AttachHand": ["def", "def2"],
                    "Note": "Second test source",
                    "Imprecise": true,
                    "Anonymised": false,
                    "ASN": [15, 231],
                    "Router": ["router1", "router2"],
                    "Netname": ["example:EXAMPLE", "example2:EXAMPLE2"],
                    "Ref": ["sourceref.example.com", "sorceref.other.example.com"]
                }
            ],
        "Target":
            [
                {
                    "Type": ["Open"],
                    "Hostname": ["targethostexample.com", "targetnameexample.com"],
                    "IP4": ["0.184.216.119"],
                    "IP6": ["0:db8::2:1", "2001:db8:a::123/64"],
                    "MAC": ["00:00:45:67:89:ab", "00:23:45:67:89:ed"],
                    "Email": ["example00@example.com", "example000@example2.com"],
                    "Proto": ["tcp", "epmap"],
                    "Port": [80],
                    "URL": ["http://www.targetexample.com", "http://www.target.otherexample.com"],
                    "Spoofed": true,
                    "AttachHand": ["att1", "att2"],
                    "Note": "First test target",
                    "Imprecise": true,
                    "Anonymised": false,
                    "ASN": [15, 231],
                    "Router": ["router3", "router4"],
                    "Netname": ["example:EXAMPLE", "example2:EXAMPLE2"],
                    "Ref": ["tar.example.com", "other.example.com"]
                },
                {
                    "Type": ["Open"],
                    "Hostname": ["example.com", "othertarget.com"],
                    "IP4": ["0.0.216.119"],
                    "IP6": ["0:0::2:1", "00:db8:a::123/64"],
                    "MAC": ["00:00:00:67:89:ab", "00:23:45:67:89:fd"],
                    "Email": ["example00@example.com", "example000@example2.com"],
                    "Proto": ["tcp2", "epmap2"],
                    "Port": [210, 542],
                    "URL": ["http://www.targetxmpl.com", "http://www.target.otherexample.com"],
                    "Spoofed": false,
                    "AttachHand": ["att3", "att4"],
                    "Note": "Second test target",
                    "Imprecise": true,
                    "Anonymised": true,
                    "ASN": [15, 231],
                    "Router": ["router5", "router6"],
                    "Netname": ["example:EXAMPLE", "example2:EXAMPLE2"],
                    "Ref": ["target.example.com", "ref.other.example.com"]
                }
            ],
        "Attach":
            [
                {
                    "Handle": "att1",
                    "FileName": ["file1.txt", "file2"],
                    "Type": ["Malware"],
                    "Hash": ["sha1:794467071687f7c59d033f4de5ece6b46415b633",
                             "md5:dc89f0b4ff9bd3b061dd66bb66c991b1"],
                    "Size": 200,
                    "Ref": ["example.com", "other.example.com"],
                    "Note": "First test attach",
                    "ContentType": ["mediatype"],
                    "ContentCharset": "UTF-8",
                    "ContentEncoding": "base64",
                    "Content": "This is content of the attach",
                    "ContentID": ["1", "2"],
                    "ExternalURI": ["external.example.com"]
                },
                {
                    "Handle": "att2",
                    "FileName": ["file1.txt", "file2"],
                    "Type": ["Malware"],
                    "Hash": ["sha1:794467071687f7c59d033f4de5ece6b46415b604",
                             "md5:dc89f0b4ff9bd3b061dd66bb66c99100"],
                    "Size": 300,
                    "Ref": ["example.com", "other.example.com"],
                    "Note": "First test attach",
                    "ContentType": ["mediatype"],
                    "ContentCharset": "UTF-8",
                    "ContentEncoding": "base64",
                    "Content": "This is content of the attach",
                    "ContentID": ["1", "2"],
                    "ExternalURI": ["external.example.com"]
                },
                {
                    "Handle": "att3",
                    "FileName": ["file1.txt", "file2"],
                    "Type": ["Malware"],
                    "Hash": ["sha1:794467071687f7c59d033f4de5ece6b46415b601",
                             "md5:dc89f0b4ff9bd3b061dd66bb66c99102"],
                    "Size": 400,
                    "Ref": ["example.com", "other.example.com"],
                    "Note": "Second test attach",
                    "ContentType": ["mediatype"],
                    "ContentCharset": "UTF-8",
                    "ContentEncoding": "base64",
                    "Content": "This is content of the attach",
                    "ContentID": ["1", "2"],
                    "ExternalURI": ["external.example.com"]
                }
            ],
        "Node":
            [
                {
                    "Name": "com.example.specific",
                    "Type": ["Log", "Statistical"],
                    "SW": ["Example software", "Example software 2"],
                    "AggrWin": "536D10:20:30.5",
                    "Note": "First test node"
                },
                {
                    "Name": "com.example.node",
                    "Type": ["Log", "Statistical"],
                    "SW": ["Example software"],
                    "AggrWin": "425D10:20:35.1",
                    "Note": "Second test node"
                }
            ]
    }"""


def get_expected_dict3():
    return {
        "Format": "IDEA0",
        "ID": "123d45",
        "CorrelID": ["28421", "87955"],
        "CreateTime": "0xbc723b45.0xef449129",
        "DetectTime": "2017-03-04T15:10:52.86445Z",
        "Category": ["Phishing"],
        "Ref": ["ref.example.com"],
        "Confidence": 0.54,
        "Source":
            [
                {
                    "Hostname": ["Second name of the equipment"],
                    "IP4": ["100.184.216.130"],
                    "IP6": ["2001:db8:a::123/64"],
                    "Proto": ["Additional info of protocol"],
                    "Port": [154],
                    "Spoofed": "yes",
                    "Router": ["interfaceExample"],
                },
                {
                    "Hostname": ["Third name of the equipment"],
                    "IP4": ["78.184.216.119"],
                    "Email": ["example@example.com"],
                    "Proto": ["Additional info of protocol"],
                    "Port": [158],
                    "Router": ["interfaceExample2"],
                }
            ],
        "Target":
            [
                {
                    "Hostname": ["Fourth name of the equipment"],
                    "IP4": ["98.184.216.119", "100.89.114.119"],
                    "Proto": ["Additional info of protocol"],
                    "Port": [80],
                    "Spoofed": "no",
                    "Router": ["interfaceExample3"],
                },
                {
                    "Hostname": ["Fifth name of the equipment"],
                    "IP4": ["100.184.216.119"],
                    "MAC": ["00:00:45:67:89:ab"],
                    "Proto": ["Additional info of protocol"],
                    "Port": [90, 91, 92, 93, 94],
                    "Spoofed": "yes",
                    "Router": ["interfaceExample4"],
                }
            ],
        "Node":
            [
                {
                    "Name": "DetectorExample",
                    "SW": ["detector great 2.0 highest Linux 4.4.0-31-generic"],
                }
            ]
    }