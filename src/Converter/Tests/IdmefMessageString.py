
def get_idmef_string():
    return """<?xml version="1.0" encoding="UTF-8"?>
<idmef:IDMEF-Message version="1.0"
                     xmlns:idmef="http://iana.org/idmef">
    <idmef:Alert messageid="123d45">
        <idmef:Analyzer analyzerid="5468" name="DetectorExample" manufacturer="Great s.r.o" model="detector great"
                        version="2.0" class="highest" ostype="Linux" osversion="4.4.0-31-generic">
            <idmef:Node ident="6" category="hosts">
                <idmef:location>
                    Location of the equipment
                </idmef:location>
                <idmef:name>
                    Name of the equipment
                </idmef:name>
                <idmef:Address ident="11" category="ipv4-addr" vlan-name="Virtual LAN example name" vlan-num="3">
                    <idmef:address>
                        93.184.216.119
                    </idmef:address>
                    <idmef:netmask>
                        255.0.0.0
                    </idmef:netmask>
                </idmef:Address>
                <idmef:Address ident="12" category="ipv4-addr" vlan-name="Virtual LAN example name" vlan-num="4">
                    <idmef:address>
                        100.184.216.119
                    </idmef:address>
                    <idmef:netmask>
                        255.255.0.0
                    </idmef:netmask>
                </idmef:Address>
            </idmef:Node>
            <idmef:Process ident="29">
                <idmef:name>
                    Program
                </idmef:name>
                <idmef:pid>
                    1482
                </idmef:pid>
                <idmef:path>
                    /path/to/program
                </idmef:path>
                <idmef:arg>
                    cmdarg1
                </idmef:arg>
                <idmef:arg>
                    cmdarg2
                </idmef:arg>
                <idmef:env>
                    VAR1=first
                </idmef:env>
                <idmef:env>
                    VAR2=second
                </idmef:env>
            </idmef:Process>
        </idmef:Analyzer>
        <idmef:CreateTime ntpstamp="0xbc723b45.0xef449129">
            2000-03-09T10:01:25.93464-05:00
        </idmef:CreateTime>
        <idmef:Classification ident="1" text="Phishing">
            <idmef:Reference origin="vendor-specific" meaning="meaning of reference">
                <idmef:name>
                    Name of alert
                </idmef:name>
                <idmef:url>
                    ref.example.com
                </idmef:url>
            </idmef:Reference>
        </idmef:Classification>
        <idmef:DetectTime ntpstamp="2017-03-04T15:10:52.86445Z">
            2017-03-04T15:10:52.86445Z
        </idmef:DetectTime>
        <idmef:AnalyzerTime ntpstamp="2017-03-03T19:10:52.86445Z">
            2017-03-03T19:10:52.86445Z
        </idmef:AnalyzerTime>
        <idmef:Source ident="2" spoofed="yes" interface="interfaceExample">
            <idmef:Node ident="7" category="coda">
                <idmef:location>
                    Second location of the equipment
                </idmef:location>
                <idmef:name>
                    Second name of the equipment
                </idmef:name>
                <idmef:Address ident="13" category="ipv6-addr" vlan-name="Virtual LAN example name" vlan-num="3">
                    <idmef:address>
                        2001:db8:a::123/64
                    </idmef:address>
                    <idmef:netmask>
                        255.0.0.0
                    </idmef:netmask>
                </idmef:Address>
                <idmef:Address ident="14" category="ipv4-addr" vlan-name="Virtual LAN example name" vlan-num="4">
                    <idmef:address>
                        100.184.216.130
                    </idmef:address>
                    <idmef:netmask>
                        255.255.0.0
                    </idmef:netmask>
                </idmef:Address>
            </idmef:Node>
            <idmef:User ident="21" category="application">
                <idmef:UserId ident="22" type="current-user" tty="/dev/pts/0">
                    <idmef:name>
                        UserName
                    </idmef:name>
                    <idmef:number>
                        51
                    </idmef:number>
                </idmef:UserId>
            </idmef:User>
            <idmef:Process ident="30">
                <idmef:name>
                    SourceProgram
                </idmef:name>
                <idmef:pid>
                    1152
                </idmef:pid>
                <idmef:path>
                    /path/to/sourceprogram
                </idmef:path>
                <idmef:arg>
                    cmdarg1
                </idmef:arg>
                <idmef:arg>
                    cmdarg2
                </idmef:arg>
                <idmef:env>
                    VARSRC1=first
                </idmef:env>
                <idmef:env>
                    VARSRC2=second
                </idmef:env>
            </idmef:Process>
            <idmef:Service ident="34" ip_version="4" iana_protocol_number="100" iana_protocol_name="protocolexample">
                <idmef:name>
                    ServiceName
                </idmef:name>
                <idmef:port>
                    154
                </idmef:port>
                <idmef:protocol>
                    Additional info of protocol
                </idmef:protocol>
                <idmef:SNMPService>
                    <idmef:oid>
                        objectident1
                    </idmef:oid>
                    <idmef:messageProcessingModel>
                        2
                    </idmef:messageProcessingModel>
                    <idmef:securityModel>
                        1
                    </idmef:securityModel>
                    <idmef:securityName>
                        SecuritynameExample
                    </idmef:securityName>
                    <idmef:securityLevel>
                        1
                    </idmef:securityLevel>
                    <idmef:contextName>
                        ContextnameExample
                    </idmef:contextName>
                    <idmef:contextEngineID>
                        ContextEngineID1
                    </idmef:contextEngineID>
                    <idmef:command>
                        GET
                    </idmef:command>
                </idmef:SNMPService>
                <idmef:WebService>
                    <idmef:url>
                        service.example.com
                    </idmef:url>
                    <idmef:cgi>
                        CGI script example
                    </idmef:cgi>
                    <idmef:http-method>
                        GET
                    </idmef:http-method>
                    <idmef:arg>
                        Argument1ToScript
                    </idmef:arg>
                    <idmef:arg>
                        Argument2ToScript
                    </idmef:arg>
                </idmef:WebService>
            </idmef:Service>
        </idmef:Source>
        <idmef:Source ident="3" spoofed="unknown" interface="interfaceExample2">
            <idmef:Node ident="8" category="dns">
                <idmef:location>
                    Third location of the equipment
                </idmef:location>
                <idmef:name>
                    Third name of the equipment
                </idmef:name>
                <idmef:Address ident="15" category="ipv4-addr" vlan-name="Virtual LAN example name" vlan-num="10">
                    <idmef:address>
                        78.184.216.119
                    </idmef:address>
                    <idmef:netmask>
                        255.255.154.0
                    </idmef:netmask>
                </idmef:Address>
                <idmef:Address ident="16" category="e-mail" vlan-name="Virtual LAN example name" vlan-num="4">
                    <idmef:address>
                        example@example.com
                    </idmef:address>
                    <idmef:netmask>
                        255.255.252.0
                    </idmef:netmask>
                </idmef:Address>
            </idmef:Node>
            <idmef:User ident="23" category="os-device">
                <idmef:UserId ident="24" type="current-group" tty="/dev/pts/0">
                    <idmef:name>
                        GroupName
                    </idmef:name>
                    <idmef:number>
                        14
                    </idmef:number>
                </idmef:UserId>
            </idmef:User>
            <idmef:Process ident="31">
                <idmef:name>
                    SourceProgram2
                </idmef:name>
                <idmef:pid>
                    1482
                </idmef:pid>
                <idmef:path>
                    /path/to/sourceprogram2
                </idmef:path>
                <idmef:arg>
                    cmdarg1
                </idmef:arg>
                <idmef:arg>
                    cmdarg2
                </idmef:arg>
                <idmef:env>
                    VARSRC1=first
                </idmef:env>
                <idmef:env>
                    VARSRC2=second
                </idmef:env>
            </idmef:Process>
            <idmef:Service ident="35" ip_version="4" iana_protocol_number="150" iana_protocol_name="protocolexample2">
                <idmef:name>
                    ServiceName2
                </idmef:name>
                <idmef:port>
                    158
                </idmef:port>
                <idmef:protocol>
                    Additional info of protocol
                </idmef:protocol>
                <idmef:SNMPService>
                    <idmef:oid>
                        objectident2
                    </idmef:oid>
                    <idmef:messageProcessingModel>
                        3
                    </idmef:messageProcessingModel>
                    <idmef:securityModel>
                        2
                    </idmef:securityModel>
                    <idmef:securityName>
                        SecuritynameExample
                    </idmef:securityName>
                    <idmef:securityLevel>
                        1
                    </idmef:securityLevel>
                    <idmef:contextName>
                        ContextnameExample1
                    </idmef:contextName>
                    <idmef:contextEngineID>
                        ContextEngineID2
                    </idmef:contextEngineID>
                    <idmef:command>
                        GET
                    </idmef:command>
                </idmef:SNMPService>
                <idmef:WebService>
                    <idmef:url>
                        service.example.com
                    </idmef:url>
                    <idmef:cgi>
                        CGI script example
                    </idmef:cgi>
                    <idmef:http-method>
                        GET
                    </idmef:http-method>
                    <idmef:arg>
                        Argument1ToScript
                    </idmef:arg>
                    <idmef:arg>
                        Argument2ToScript
                    </idmef:arg>
                </idmef:WebService>
            </idmef:Service>
        </idmef:Source>
        <idmef:Target ident="4" decoy="no" interface="interfaceExample3">
            <idmef:Node ident="9" category="kerberos">
                <idmef:location>
                    Fourth location of the equipment
                </idmef:location>
                <idmef:name>
                    Fourth name of the equipment
                </idmef:name>
                <idmef:Address ident="17" category="ipv4-addr" vlan-name="Virtual LAN example name" vlan-num="1">
                    <idmef:address>
                        98.184.216.119
                    </idmef:address>
                    <idmef:netmask>
                        255.255.0.0
                    </idmef:netmask>
                </idmef:Address>
                <idmef:Address ident="18" category="ipv4-addr" vlan-name="Virtual LAN example name" vlan-num="4">
                    <idmef:address>
                        100.89.114.119
                    </idmef:address>
                    <idmef:netmask>
                        255.0.0.0
                    </idmef:netmask>
                </idmef:Address>
            </idmef:Node>
            <idmef:User ident="25" category="os-device">
                <idmef:UserId ident="26" type="original-user" tty="/dev/pts/0">
                    <idmef:name>
                        NextUserName
                    </idmef:name>
                    <idmef:number>
                        26
                    </idmef:number>
                </idmef:UserId>
            </idmef:User>
            <idmef:Process ident="32">
                <idmef:name>
                    TargetProgram
                </idmef:name>
                <idmef:pid>
                    1692
                </idmef:pid>
                <idmef:path>
                    /path/to/targetprogram
                </idmef:path>
                <idmef:arg>
                    cmdarg1
                </idmef:arg>
                <idmef:arg>
                    cmdarg2
                </idmef:arg>
                <idmef:env>
                    VARTRG1=first
                </idmef:env>
                <idmef:env>
                    VARTRG2=second
                </idmef:env>
            </idmef:Process>
            <idmef:Service ident="36" ip_version="4" iana_protocol_number="152" iana_protocol_name="protocolexample3">
                <idmef:name>
                    ServiceName3
                </idmef:name>
                <idmef:port>
                    80
                </idmef:port>
                <idmef:protocol>
                    Additional info of protocol
                </idmef:protocol>
                <idmef:SNMPService>
                    <idmef:oid>
                        objectident3
                    </idmef:oid>
                    <idmef:messageProcessingModel>
                        3
                    </idmef:messageProcessingModel>
                    <idmef:securityModel>
                        2
                    </idmef:securityModel>
                    <idmef:securityName>
                        SecuritynameExample3
                    </idmef:securityName>
                    <idmef:securityLevel>
                        1
                    </idmef:securityLevel>
                    <idmef:contextName>
                        ContextnameExample3
                    </idmef:contextName>
                    <idmef:contextEngineID>
                        ContextEngineID3
                    </idmef:contextEngineID>
                    <idmef:command>
                        GET
                    </idmef:command>
                </idmef:SNMPService>
                <idmef:WebService>
                    <idmef:url>
                        service.example.com
                    </idmef:url>
                    <idmef:cgi>
                        CGI script example
                    </idmef:cgi>
                    <idmef:http-method>
                        GET
                    </idmef:http-method>
                    <idmef:arg>
                        Argument1ToScript
                    </idmef:arg>
                    <idmef:arg>
                        Argument2ToScript
                    </idmef:arg>
                </idmef:WebService>
            </idmef:Service>
            <idmef:File ident="62" category="current" fstype="ufs" file-type="Filetype">
                <idmef:name>
                    FileName
                </idmef:name>
                <idmef:path>
                    fileserver:/path/to/FileName
                </idmef:path>
                <idmef:create-time>
                    2017-10-25T11:00:51
                </idmef:create-time>
                <idmef:modify-time>
                    2017-10-25T11:00:52
                </idmef:modify-time>
                <idmef:access-time>
                    2017-10-25T11:00:53
                </idmef:access-time>
                <idmef:data-size>
                    542
                </idmef:data-size>
                <idmef:disk-size>
                    546
                </idmef:disk-size>
                <idmef:FileAccess>
                    <idmef:UserId ident="60" type="user-privs" tty="/dev/pts/0">
                        <idmef:name>
                            LastUserName
                        </idmef:name>
                        <idmef:number>
                            30
                        </idmef:number>
                    </idmef:UserId>
                    <idmef:Permission perms="read">
                    </idmef:Permission>
                    <idmef:Permission perms="write">
                    </idmef:Permission>
                </idmef:FileAccess>
                <idmef:Linkage category="hard-link">
                    <idmef:name>
                        FsObject
                    </idmef:name>
                    <idmef:path>
                        /path/to/FsObject
                    </idmef:path>
                </idmef:Linkage>
                <idmef:Inode>
                    <idmef:change-time>
                        2017-10-25T11:00:58
                    </idmef:change-time>
                    <idmef:number>
                        5268
                    </idmef:number>
                    <idmef:c-major-device>
                        2173
                    </idmef:c-major-device>
                </idmef:Inode>
                <idmef:Checksum algorithm="SHA1">
                    <idmef:value>
                        794467071687f7c59d033f4de5ece6b46415b601
                    </idmef:value>
                    <idmef:key>
                        chckey
                    </idmef:key>
                </idmef:Checksum>
            </idmef:File>
            <idmef:File ident="63" category="current" fstype="ufs" file-type="Filetype">
                <idmef:name>
                    FileName
                </idmef:name>
                <idmef:path>
                    fileserver:/path/to/FileName
                </idmef:path>
                <idmef:create-time>
                    2017-10-25T11:00:51
                </idmef:create-time>
                <idmef:modify-time>
                    2017-10-25T11:00:52
                </idmef:modify-time>
                <idmef:access-time>
                    2017-10-25T11:00:53
                </idmef:access-time>
                <idmef:data-size>
                    542
                </idmef:data-size>
                <idmef:disk-size>
                    546
                </idmef:disk-size>
                <idmef:FileAccess>
                    <idmef:UserId ident="51" type="user-privs" tty="/dev/pts/0">
                        <idmef:name>
                            LastUserName
                        </idmef:name>
                        <idmef:number>
                            30
                        </idmef:number>
                    </idmef:UserId>
                    <idmef:Permission perms="read">
                    </idmef:Permission>
                    <idmef:Permission perms="write">
                    </idmef:Permission>
                </idmef:FileAccess>
                <idmef:Linkage category="hard-link">
                    <idmef:name>
                        FsObject
                    </idmef:name>
                    <idmef:path>
                        /path/to/FsObject
                    </idmef:path>
                </idmef:Linkage>
                <idmef:Inode>
                    <idmef:change-time>
                        2017-10-25T11:00:58
                    </idmef:change-time>
                    <idmef:number>
                        5268
                    </idmef:number>
                    <idmef:c-major-device>
                        2173
                    </idmef:c-major-device>
                </idmef:Inode>
                <idmef:Checksum algorithm="SHA1">
                    <idmef:value>
                        794467071687f7c59d033f4de5ece6b46415b601
                    </idmef:value>
                    <idmef:key>
                        chckey
                    </idmef:key>
                </idmef:Checksum>
            </idmef:File>
        </idmef:Target>
        <idmef:Target ident="5" decoy="yes" interface="interfaceExample4">
            <idmef:Node ident="10" category="hosts">
                <idmef:location>
                    Fifth location of the equipment
                </idmef:location>
                <idmef:name>
                    Fifth name of the equipment
                </idmef:name>
                <idmef:Address ident="19" category="ipv4-addr" vlan-name="Virtual LAN example name" vlan-num="4">
                    <idmef:address>
                        100.184.216.119
                    </idmef:address>
                    <idmef:netmask>
                        255.255.0.0
                    </idmef:netmask>
                </idmef:Address>
                <idmef:Address ident="20" category="e-mail" vlan-name="Virtual LAN example name" vlan-num="1">
                    <idmef:address>
                        example2@example.com
                    </idmef:address>
                    <idmef:netmask>
                        255.255.255.10
                    </idmef:netmask>
                </idmef:Address>
            </idmef:Node>
            <idmef:User ident="27" category="os-device">
                <idmef:UserId ident="28" type="target-user" tty="/dev/pts/0">
                    <idmef:name>
                        LastUserName
                    </idmef:name>
                    <idmef:number>
                        30
                    </idmef:number>
                </idmef:UserId>
            </idmef:User>
            <idmef:Process ident="33">
                <idmef:name>
                    TargetProgram2
                </idmef:name>
                <idmef:pid>
                    2103
                </idmef:pid>
                <idmef:path>
                    /path/to/targetprogram2
                </idmef:path>
                <idmef:arg>
                    cmdarg1
                </idmef:arg>
                <idmef:arg>
                    cmdarg2
                </idmef:arg>
                <idmef:env>
                    VARTRG1=first
                </idmef:env>
                <idmef:env>
                    VARTRG2=second
                </idmef:env>
            </idmef:Process>
            <idmef:Service ident="37" ip_version="4" iana_protocol_number="90" iana_protocol_name="protocolexample4">
                <idmef:name>
                    ServiceName3
                </idmef:name>
                <idmef:port>
                    90
                </idmef:port>
                <idmef:protocol>
                    Additional info of protocol
                </idmef:protocol>
                <idmef:SNMPService>
                    <idmef:oid>
                        objectident4
                    </idmef:oid>
                    <idmef:messageProcessingModel>
                        3
                    </idmef:messageProcessingModel>
                    <idmef:securityModel>
                        2
                    </idmef:securityModel>
                    <idmef:securityName>
                        SecuritynameExample4
                    </idmef:securityName>
                    <idmef:securityLevel>
                        1
                    </idmef:securityLevel>
                    <idmef:contextName>
                        ContextnameExample4
                    </idmef:contextName>
                    <idmef:contextEngineID>
                        ContextEngineID4
                    </idmef:contextEngineID>
                    <idmef:command>
                        GET
                    </idmef:command>
                </idmef:SNMPService>
                <idmef:WebService>
                    <idmef:url>
                        service.example.com
                    </idmef:url>
                    <idmef:cgi>
                        CGI script example
                    </idmef:cgi>
                    <idmef:http-method>
                        GET
                    </idmef:http-method>
                    <idmef:arg>
                        Argument1ToScript
                    </idmef:arg>
                    <idmef:arg>
                        Argument2ToScript
                    </idmef:arg>
                </idmef:WebService>
            </idmef:Service>
            <idmef:File ident="38" category="current" fstype="ufs" file-type="Filetype">
                <idmef:name>
                    FileName
                </idmef:name>
                <idmef:path>
                    fileserver:/path/to/FileName
                </idmef:path>
                <idmef:create-time>
                    2017-10-25T11:00:51
                </idmef:create-time>
                <idmef:modify-time>
                    2017-10-25T11:00:52
                </idmef:modify-time>
                <idmef:access-time>
                    2017-10-25T11:00:53
                </idmef:access-time>
                <idmef:data-size>
                    542
                </idmef:data-size>
                <idmef:disk-size>
                    546
                </idmef:disk-size>
                <idmef:FileAccess>
                    <idmef:UserId ident="54" type="user-privs" tty="/dev/pts/0">
                        <idmef:name>
                            LastUserName
                        </idmef:name>
                        <idmef:number>
                            30
                        </idmef:number>
                    </idmef:UserId>
                    <idmef:Permission perms="read">
                    </idmef:Permission>
                    <idmef:Permission perms="write">
                    </idmef:Permission>
                </idmef:FileAccess>
                <idmef:Linkage category="hard-link">
                    <idmef:name>
                        FsObject
                    </idmef:name>
                    <idmef:path>
                        /path/to/FsObject
                    </idmef:path>
                </idmef:Linkage>
                <idmef:Inode>
                    <idmef:change-time>
                        2017-10-25T11:00:58
                    </idmef:change-time>
                    <idmef:number>
                        5268
                    </idmef:number>
                    <idmef:c-major-device>
                        2173
                    </idmef:c-major-device>
                </idmef:Inode>
                <idmef:Checksum algorithm="SHA1">
                    <idmef:value>
                        794467071687f7c59d033f4de5ece6b46415b601
                    </idmef:value>
                    <idmef:key>
                        chckey
                    </idmef:key>
                </idmef:Checksum>
            </idmef:File>
            <idmef:File ident="50" category="current" fstype="ufs" file-type="Filetype">
                <idmef:name>
                    FileName
                </idmef:name>
                <idmef:path>
                    fileserver:/path/to/FileName
                </idmef:path>
                <idmef:create-time>
                    2017-10-25T11:00:51
                </idmef:create-time>
                <idmef:modify-time>
                    2017-10-25T11:00:52
                </idmef:modify-time>
                <idmef:access-time>
                    2017-10-25T11:00:53
                </idmef:access-time>
                <idmef:data-size>
                    542
                </idmef:data-size>
                <idmef:disk-size>
                    546
                </idmef:disk-size>
                <idmef:FileAccess>
                    <idmef:UserId ident="51" type="user-privs" tty="/dev/pts/0">
                        <idmef:name>
                            LastUserName
                        </idmef:name>
                        <idmef:number>
                            30
                        </idmef:number>
                    </idmef:UserId>
                    <idmef:Permission perms="read">
                    </idmef:Permission>
                    <idmef:Permission perms="write">
                    </idmef:Permission>
                </idmef:FileAccess>
                <idmef:Linkage category="hard-link">
                    <idmef:name>
                        FsObject
                    </idmef:name>
                    <idmef:path>
                        /path/to/FsObject
                    </idmef:path>
                </idmef:Linkage>
                <idmef:Inode>
                    <idmef:change-time>
                        2017-10-25T11:00:58
                    </idmef:change-time>
                    <idmef:number>
                        5268
                    </idmef:number>
                    <idmef:c-major-device>
                        2173
                    </idmef:c-major-device>
                </idmef:Inode>
                <idmef:Checksum algorithm="SHA1">
                    <idmef:value>
                        794467071687f7c59d033f4de5ece6b46415b601
                    </idmef:value>
                    <idmef:key>
                        chckey
                    </idmef:key>
                </idmef:Checksum>
            </idmef:File>
        </idmef:Target>
        <idmef:Assessment>
            <idmef:Impact severity="medium" completion="succeeded" type="admin">
                Optional description of impact, which is allowed here
            </idmef:Impact>
            <idmef:Action category="taken-offline">
                Optional description of action, which is allowed here
            </idmef:Action>
            <idmef:Action category="notification-sent">
                Optional description of action, which is allowed here
            </idmef:Action>
            <idmef:Confidence rating="numeric">
                0.54
            </idmef:Confidence>
        </idmef:Assessment>
        <idmef:CorrelationAlert>
            <idmef:name>
                CorrelationExampleName
            </idmef:name>
            <idmef:alertident analyzerid="12">
                28421
            </idmef:alertident>
            <idmef:alertident analyzerid="654">
                87955
            </idmef:alertident>
        </idmef:CorrelationAlert>
        <idmef:AdditionalData meaning="Test additional data">
            First additional data test example
        </idmef:AdditionalData>
        <idmef:AdditionalData meaning="Test additional data too">
            Second additional data test example
        </idmef:AdditionalData>
    </idmef:Alert>
</idmef:IDMEF-Message>
"""