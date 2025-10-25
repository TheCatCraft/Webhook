import requests
import random
import json
import time

test = 0
test2 = 200

WEBHOOK_URL = "https://discord.com/api/webhooks/1431596654623981648/kZ8hSwpPaAOuQPJiH_6g7iaRxqegX_VM_cag4YRhezEHobMXzbYq0A-3e-97o96fl9_t"

names = [
    "Lukas", "Max", "Felix", "Leon", "Jonas", "Mia",
    "Anna", "Sophie", "Paul", "Lara", "Elias", "Emilia",
    "Nico", "Lina", "Tom", "Sara"
]

versions = [
    "1.21.10", "1.21.9", "1.21.8", "1.21.7", "1.21.6", "1.21.5", "1.21.4", "1.21.3", "1.21.2", "1.21.1",
    "1.21", "1.20.6", "1.20.5", "1.20.4", "1.20.3", "1.20.2", "1.20.1", "1.20", "1.19.4", "1.19.3",
    "1.19.2", "1.19.1", "1.19", "1.18.2", "1.18.1", "1.18", "1.17.1", "1.17", "1.16.5", "1.16.4", "1.16.3",
    "1.16.2", "1.16.1", "1.16", "1.15.2", "1.15.1", "1.15", "1.14.4", "1.14.3", "1.14.2", "1.14.1", "1.14",
    "1.13.2", "1.13.1", "1.13", "1.12.2", "1.12.1", "1.12", "1.11.2", "1.11.1", "1.11", "1.10.2", "1.10.1",
    "1.10", "1.9.4", "1.9.3", "1.9.2", "1.9.1", "1.9", "1.8.9", "1.8.8", "1.8.7", "1.8.6", "1.8.5", "1.8.4",
    "1.8.3", "1.8.2", "1.8.1", "1.8", "1.7.10", "1.7.9", "1.7.8", "1.7.7", "1.7.6", "1.7.5", "1.7.4", "1.7.3",
    "1.7.2", "1.7.1", "1.7", "1.6.4", "1.6.2", "1.6.1", "1.5.2", "1.5.1", "1.5", "1.4.7", "1.4.6", "1.4.5",
    "1.4.4", "1.4.2", "1.3.2", "1.3.1", "1.2.5", "1.2.4", "1.2.3", "1.2.2", "1.2.1", "1.1", "1.0.0", "b1.9-pre5",
    "b1.9-pre4", "b1.9-pre3", "b1.9-pre2", "b1.9-pre1", "b1.8.1", "b1.8", "b1.7.3", "b1.7.2", "b1.7.1", "b1.6.6",
    "b1.6.5", "b1.6.4", "b1.6.3", "b1.6.2", "b1.6.1", "b1.5_02", "b1.5_01", "b1.5", "b1.4_01", "b1.4", "b1.3_01",
    "b1.3", "b1.2_02", "b1.2_01", "b1.2", "b1.1_02", "b1.1_01", "b1.1", "b1.0_02", "b1.0_01", "b1.0", "a1.2_02",
    "a1.2_01", "a1.2", "a1.1_02", "a1.1_01", "a1.1", "a1.0_02", "a1.0_01", "a1.0"  # Snapshot-Versionen
]

title = [
    "Kenny", "RGB-Bibel", "Steam-Truck", "My-Back", "WIN", "WIN1", "WIN2", "WIN3", "WIN4", "Test", "Developer", "Gründer", "Supporter", "Admin",
]

kenny = [
    "d:/Lokal E/APPs/Python/requests/20.mp4", "d:/Lokal E/APPs/Python/requests/18.mp4"
]

steamtruck = [
    "d:/Lokal E/APPs/Python/requests/3.mp4", "d:/Lokal E/APPs/Python/requests/5.mp4"
]


while test < test2:
    random_name = random.choice(names) + str(random.randint(10, 999))
    random_age = random.randint(13, 999)
    random_version = random.choice(versions)#str(random.randint(0, 2)) + "." + str(random.randint(0, 99)) + "." + str(random.randint(0, 99))
    random_title = random.choice(title)
    random_er = random_age - random.randint(13, 999)

    try:
        if random_title == "RGB-Bibel":
            payload = {
                "username": "RG-BIST",
                "content": "🌈 **Die hell erleuchteten 10-RGBote der RGBibel** 🌈",
                "embeds": [
                    {
                        "title": "💡 Die 10-RGBote 💡",
                        "description": "1️⃣ Du sollst keine Apple-Produkte kaufen.\n2️⃣ Mehr RGB, mehr FPS.\n3️⃣ Du sollst die RGB-Stripes ehren wie deine eigenen RGB-Lüfter.\n4️⃣ Gaming-PCs werden immer selbst gebaut.\n5️⃣ Du sollst dich deiner Rainbow-Tastatur gleichstellen.\n6️⃣ Du sollst die 16,7 Millionen Farben ehren und kennen.\n7️⃣ Du sollst die deinesgleichen stets mit einem LED-Band beschenken.\n8️⃣ Kein Preis ist für eine gute RGB-Beleuchtung zu hoch.\n9️⃣ Der Threadripper ist kein Gaming-Prozessor.\n🔟 Eine Wasserkühlung sollte stets gefärbt sein.",
                        "color": 16711884,
                        "image": {
                            "url": "https://i.imgur.com/33jMMpw.jpg"
                        }
                    },
                    {
                        "title": "🙏 Vater unser im Leuchten 🙏",
                        "description": "Vater unser im Leuchten,\nGeheiligt werde dein RGB.\nDein Win komme,\ndeine K/D profitiere,\nWie in Fortnite, so in PUBG.\n\nUnser tägliches RGB gib uns heute,\nUnd vergib uns unsere RGB-Sünden,\nWie auch wir vergeben unseren Noobs.\n\nUnd führe uns nicht in Minecraft,\nSondern erlöse uns vom Microsoft-Store.\n\nDenn dein ist das Leuchten und die RGBibel,\n**Amen.** 🌈✨",
                        "color": 65280,
                        "footer": {
                            "text": "Die hell erleuchteten 10-RGBote · © RGBibel"
                        },
                        "image": {
                            "url": "https://i.imgur.com/35mW0ah.gif"
                        }
                    }
                ]
            }
            response = requests.post(WEBHOOK_URL, json=payload)

        elif random_title == "Kenny":
            random_kenny = random.choice(kenny)

            with open(random_kenny, "rb") as f:
                payload = {"username": "KennyTV",}
                files = {"file": f}
                response = requests.post(WEBHOOK_URL, files=files, json=payload)
        
        elif random_title == "Steam-Truck":
            random_steamtruck = random.choice(steamtruck)

            with open(random_steamtruck, "rb") as f:
                payload = {"username": "ECO HATER",}
                files = {"file": f}
                response = requests.post(WEBHOOK_URL, files=files, json=payload)

        elif random_title == "My-Back":
            payload = {
                "username": "Schiopraktika",
                "embeds": [
                    {
                        "title": "AAAAAAAAAAAAAAAAHHHHHHHHHH",
                        "description": "MY BACK",
                        "color": 16711884,
                        "image": {
                            "url": "https://cdn.discordapp.com/attachments/770293678131642369/1431413497140477993/imagasde.png?ex=68fd5334&is=68fc01b4&hm=c509f54387123244b62d07d3d36a7c19796b554d4e24c9b22b88eea511ed081c&"
                        }
                    }
                ]
            }
            response = requests.post(WEBHOOK_URL, json=payload)

        elif random_title == "WIN":
            payload = {
                "username": "NT History",
                "embeds": [
                    {
                    "title": "Windows NT 3.1 April 1991 Build",
                    "description": "The Windows NT 3.1 April 1991 build is an otherwise unidentified early build of Windows NT 3.1, which is currently the earliest available build of Windows NT overall. Disk images labeled \"WOW Reversi MIPS Demo\" that contain ZIP archives with the build's files were added to the PCjs miscellaneous diskette repository on 4 November 2023 by Jeff Parsons, the developer of the PCjs website and a former Microsoft employee. The build is compiled for an early version of the Microsoft Jazz architecture that predates the launch of the MIPS R4000 processor. As such, it actually targets the earlier R3000 processor, which is not fully compatible with the R4000. The build was used for an internal demonstration of Reversi running under Windows on Windows and x86 emulation on a MIPS machine during a weekly \"Thursday Beers\" event."
                    },
                    {
                    "title": "Graphics & GDI",
                    "description": "This demonstration was memorable for Reversi displaying square pieces rather than round, because GDI couldn't draw circles or curves yet. The primitives implemented by this build's GDI only include lines, rectangles and text. Furthermore, only solid color brushes are supported. According to internal conversations, GDI was not planned to be code complete until June 1991."
                    },
                    {
                    "title": "Windows-on-Windows & Console",
                    "description": "This build is the earliest known to include Windows-on-Windows (WoW), a compatibility layer allowing 32-bit Windows to run 16-bit DOS and Windows applications. The 16-bit components run in real mode. Console mode exists but cannot run simultaneously with the SM prompt, and early Win32 API implementations are very limited.",
                        "image": {
                            "url": "https://cdn.discordapp.com/attachments/770293678131642369/1431413010131456031/MicrosoftPlus-4.png?ex=68fd52bf&is=68fc013f&hm=db9e21980c97d6a03ac992c792db506d0f17f644fc4a27b1a05db6bcf6d00ffe&"
                        }
                    },
                    
                ]
            }
            response = requests.post(WEBHOOK_URL, json=payload)

        elif random_title == "WIN1":
            payload = {
                "username": "Windows History",
                "embeds": [
                    {
                    "title": "Microsoft Cairo Project",
                    "description": "Cairo was the codename of an unreleased software project by Microsoft, intended to bring next-generation technologies to Windows NT. The project was originally announced at the 1991 PDC (Professional Developers Conference) and later demoed at the 1993 PDC. The Cairo project consisted of a revamped core operating system, as well as new services and server tools to ship alongside the core OS. Initially, the core OS would be based on Windows NT 3.1 and later Windows NT 3.5x, but after Windows 95 adopted the Cairo UI, it was pushed back to target what became Windows NT 4.0 instead."
                    },
                    {
                    "title": "Core OS and Services",
                    "description": "The core OS focused on improving upon NT 3.1's user interface (with enhancements such as a new desktop, Smart Folders, the Explorer, drag-and-drop, and context menus) while remaining compatible with existing Windows applications. The included services and server tools focused on improving network capabilities and support for domains, networked storage, network communication, printer sharing, and distributed computing. Cairo development continued through until 1996, after which the project was canceled."
                    },
                    {
                    "title": "Legacy",
                    "description": "Many components slated for Cairo (such as the user interface) were instead repurposed for Windows 95, which continued the Windows-on-DOS line. Windows NT 4.0 later shipped with the Windows 95 shell and already-released Cairo components. The remaining components from Cairo influenced future Windows projects, such as the canceled WinFS and Active Directory."
                    },
                    {
                    "title": "SKUs",
                    "description": "Three different retail SKUs were planned for Microsoft Cairo, all aimed at the enterprise market:\n\n- Cairo Advanced Desktop: Core OS, new UI, networked storage/printer sharing.\n- Cairo Advanced Server: All features of Desktop + server roles, domain services, network messaging, management tools.\n- Cairo Design Environment: Tools for developers to build Cairo applications, including Smart Folders SDK, authoring tools, debugger, documentation, and VBA."
                    },
                    {
                    "title": "Known Components",
                    "description": "**Windows NT 3.1:** DCE RPC, COM, OLE\n\n**Windows NT 3.5x / 4.0:** Cairo OFS (Object File System), Cairo OFS Indexing, Cairo Domains (x.500, later Active Directory)\n\n**Windows 95 / NT 4.0 / Other:** Cairo User Interface (later Windows 95/NT4 Shell), Cairo Messaging (x.400, later Exchange), Cairo Smart Folders (influence on Windows 7 Libraries)",
                        "image": {
                            "url": "https://cdn.discordapp.com/attachments/770293678131642369/1431416716562530406/290px-Windows_NT_3.png?ex=68fd5633&is=68fc04b3&hm=5818642c43f2c4658902382529443bc10f46f396948fbc4a1f0648aa90ced5e5&"
                        }
                    }
                ]
            }
            response = requests.post(WEBHOOK_URL, json=payload)

        elif random_title == "WIN2":
            payload = {
                "username": "Mac OS History",
                "embeds": [
                    {
                    "title": "Mac OS X Server 1.x Overview",
                    "description": "Mac OS X Server 1.x is the first operating system commercially released by Apple based on NeXT technology. It originated from the Rhapsody project, which aimed to run all existing classic Mac OS code in a virtual machine, requiring major application rewrites to run natively."
                    },
                    {
                    "title": "Development",
                    "description": "The Rhapsody project was announced on 7 January 1997 at MacWorld Expo and demonstrated at the 1997 WWDC. It represented the fifth major version of UNIX-based NeXTSTEP following Apple's acquisition of NeXT. Rhapsody included 'Blue Box' for emulated Mac OS 8 apps and 'Yellow Box' for native apps using NeXTSTEP libraries. Due to developer backlash, the project shifted focus to a server OS, introducing the Carbon API and later Cocoa."
                    },
                    {
                    "title": "Release and Support",
                    "description": "Mac OS X Server 1.0 shipped to the public on 16 March 1999 and was supported until 2001. Updated versions supported PowerPC G4 systems. This release was the first to feature NetBoot. The NeXTSTEP codebase became the foundation of Darwin, forming the core of future Mac OS X releases. Carbon API support was incorporated into the Mac OS X Public Beta."
                    },
                    {
                    "title": "Version Branding",
                    "description": "Each build of Mac OS X Server 1.x referred to itself as 'Rhapsody' in the kernel, even after developer releases."
                    },
                    {
                    "title": "Known Builds",
                    "description": "- Rhapsody Developer Release 1: 5.0, Grail, 1997-10-13, first public release for PowerPC\n- Rhapsody Developer Release 2: 5.1, Titan, 1998-05-14, last public release for i386\n- Rhapsody 1.0: 5.2, never publicly released\n- Mac OS X Server 1.0: 5.3, Hera, 1999-03-16\n- Mac OS X Server 1.0.1: 5.4, Loki, 1999-04-15\n- Mac OS X Server 1.0.2: 5.5, 1999-07-29\n- Mac OS X Server 1.2: 5.6, Pele, 2000-01-14\n- Mac OS X Server 1.2 v3: 5.6, Medusa, 2000-10-27",
                        "image": {
                            "url": "https://cdn.discordapp.com/attachments/770293678131642369/1431417880137830611/Windows1Byte.png?ex=68fd5749&is=68fc05c9&hm=6f6b5b4a94ec2ca6bf95b8d51c4cd5359d1ba11df79bcc5cd22112d89d86b6d5&"
                        }
                    }
                ]
            }

            response = requests.post(WEBHOOK_URL, json=payload)
            
        elif random_title == "WIN3":
            payload = {
                "username": "OS/2 History",
                "embeds": [
                    {
                    "title": "OS/2 1.0 Overview",
                    "description": "OS/2 1.0 is the first version of OS/2 to be released. It was originally meant to be DOS 5.0, and some early documentation refers to it as 'DOS 5.0'. This release did not include a GUI."
                    },
                    {
                    "title": "History",
                    "description": "OS/2 development began in January 1983 as a real-mode, preemptively multitasked fork of MS-DOS 2.0, eventually released as Multitasking MS-DOS 4. After the IBM-Microsoft Joint Development Agreement in August 1985, DOS 4.0 was split into two projects: 'DOS 5.0' and versions for OEMs. On 2 April 1987, OS/2 1.0 was announced with an initial release planned for early 1988, followed by OS/2 1.1 later that year. The OS leveraged IBM PS/2 systems alongside AT-compatible PCs."
                    },
                    {
                    "title": "SDK and Pre-Releases",
                    "description": "Microsoft shipped OS/2 SDK 1.00 in May 1987, providing pre-release versions for developers at $3000. SDK 1.01 in August 1987 added the Program Selector interface, and SDK 1.02 contained the final build. These SDKs allowed developers to compile software for OS/2 before its public release."
                    },
                    {
                    "title": "Release and Features",
                    "description": "OS/2 1.0 was released in December 1987, marketed as the successor to DOS and as a transitional OS. It supported dual booting with DOS, introduced a new API library to handle hardware instructions directly, and ran in protected mode (though setup used real mode). OS/2 1.0 leveraged 286 processor features such as segmented memory and multithreading but did not utilize 386 features like virtual 8086 mode or 32-bit applications."
                    },
                    {
                    "title": "Reception and Legacy",
                    "description": "OS/2 1.0 received mixed reviews: praised for expanding processor capabilities but criticized for poor DOS compatibility. It sold poorly in the consumer market but decently in corporate environments. Despite lacking a GUI, it allowed direct display access through the Vio library, later deprecated in 32-bit OS/2 versions. OS/2 1.1, released in 1988, added a proper GUI.",
                        "image": {
                            "url": "https://cdn.discordapp.com/attachments/770293678131642369/1431418548076679238/Windows95-4.png?ex=68fd57e8&is=68fc0668&hm=0b53c218273bc58c1d2627bf8379d15e3ae17f935bd258ddc312e8babe13848e&"
                        }                
                    }
                ]
            }
            response = requests.post(WEBHOOK_URL, json=payload)

        elif random_title == "WIN4":
            payload = {
                "username": "Minecraft Reactor Troubleshooting",
                "embeds": [
                    {
                    "title": "Issue Overview",
                    "description": "Jamie (she/her) reports severe issues with a sodium-cooled fission reactor in Minecraft, describing it as one of the most poorly documented and frustrating mods she has encountered. Her reactor is not outputting steam as expected; instead, the steam builds up inside the system despite proper connections. The reactor previously overheated and required a rebuild. Jamie has tried following multiple YouTube guides and community advice, but the results remain inconsistent and misleading. She expressed a strong desire to remove the mod due to these persistent issues."
                    },
                    {
                    "title": "Reactor Configuration",
                    "description": "Jamie’s reactor is an 18x18x18 maximum size sodium-cooled fission reactor. She has set up pressurized tubes to transfer superheated sodium to a boiler, which is intended to convert the superheated sodium into steam to feed a turbine. The reactor initially ran at around 213°F with a burn rate of 10, which was later adjusted to 50 to stabilize at 263°F. She uses a closed-loop system where cooled sodium returns from the boiler back into the reactor."
                    },
                    {
                    "title": "Problems Encountered",
                    "description": "Key issues Jamie faced include:\n- Steam continuously builds without moving to the turbine.\n- Superheated sodium appears in return pipes where cooled sodium is expected.\n- The reactor still contains water despite using sodium cooling, which is incompatible.\n- Push/pull settings for the tubes do not resolve the flow problems.\n- Repeated removal and replacement of tubes (even with ultimate pressurized tubes) did not fix the issue.\n- Following YouTube tutorials caused confusion due to incorrect or incomplete guidance."
                    },
                    {
                    "title": "Community Guidance",
                    "description": "Bread, Serhan, and other community members provided extensive troubleshooting advice:\n- Return tubes should only carry cooled sodium, never superheated.\n- Water should be removed from the reactor when using sodium cooling.\n- The boiler may not be necessary if the turbine can directly receive superheated sodium.\n- Use port-to-port connections between reactor, boiler, and turbine to avoid throughput limitations.\n- Place the boiler adjacent to the reactor to simplify connections and reduce bottlenecks.\n- Verify that all tube connections are correct and the correct tube types are used (ultimate pressurized tubes)."
                    },
                    {
                    "title": "Technical Observations",
                    "description": "Jamie measured reactor temperatures in both Celsius and Fahrenheit, converting 105.75°C to approximately 222°F. She experimented with burn rates ranging from 10 to 200. A burn rate of 50 stabilized the system at 263°F, but higher burn rates caused the reactor to overheat and melt down. Bread noted that tube throughput is a limiting factor, while Serhan emphasized that even large setups could exceed tube capacities, making proper connection methods crucial. Superheated sodium should not be present in return pipes as it prevents the system from cooling efficiently."
                    },
                    {
                    "title": "User Challenges",
                    "description": "Jamie expressed being overwhelmed due to Asperger's Syndrome, ADD, and depression, which compounded the difficulty of troubleshooting the complex reactor system. She attempted to follow the community's advice, removed all input/output tubes, and repiped the system multiple times. Despite these efforts, the reactor system continued malfunctioning, leading to frustration and consideration to remove the mod entirely. She highlighted her professional IT background (MCSE, CCNA, CompTIA A+, Solaris, Linux) to argue that the problem is not due to lack of skill but rather complexity and mod mechanics."
                    },
                    {
                    "title": "Community Reflection and Feedback",
                    "description": "Community members, including Bread and Serhan, maintained that the mod works as intended and that most issues arise from misunderstandings, improper setup, and exceeding system throughput. Bread provided multiple screenshots, demonstrations, and step-by-step guidance, yet Jamie reported the setup still melted down. Other users noted that some players struggle with complex mod mechanics even with proper guides. The conversation highlighted the necessity for accurate documentation, effective tutorials, and the challenges of troubleshooting high-complexity systems in Minecraft mods."
                    },
                    {
                    "title": "Resolution Attempts",
                    "description": "Jamie attempted multiple solutions:\n- Removing all tubes from the input side.\n- Replacing tubes with ultimate pressurized tubes.\n- Adjusting burn rates.\n- Trying to stabilize the reactor temperature.\n- Following screenshots and community-provided setups exactly.\nDespite these actions, the reactor system failed to operate as intended at maximum capacity. Bread advised clearing superheated sodium from return pipes, using port-to-port connections, and simplifying the layout to reduce bottlenecks."
                    },
                    {
                    "title": "Emotional Impact",
                    "description": "Jamie expressed high levels of stress and frustration, emphasizing her mental health conditions while attempting to troubleshoot the reactor. She felt overwhelmed by conflicting advice and technical complexity. She communicated that she tried to follow guidance, but the mod's mechanics, combined with maximum reactor size and tube throughput limitations, led to repeated failures, culminating in her decision to remove the mod from her server."
                    },
                    {
                    "title": "Final Notes",
                    "description": "The conversation demonstrates the challenges of understanding and managing complex Minecraft mod systems, especially advanced multiblock structures like sodium-cooled fission reactors. It highlights the importance of clear documentation, accessible tutorials, and proper community support. While Jamie struggled despite professional IT expertise, community members reinforced that the mod functions correctly and that failures are often due to setup errors, misinterpretation of mechanics, and system limitations rather than inherent bugs.",
                        "image": {
                            "url": "https://cdn.discordapp.com/attachments/770293678131642369/1431422359746777169/58008.png?ex=68fd5b75&is=68fc09f5&hm=cfc959b91d52ef1bd1d3aae34fb127cda5ce543e74bd84345fd3c0fe197edd13&"
                        } 
                    }
                ]
            }


            response = requests.post(WEBHOOK_URL, json=payload)

        else:
            payload = {
                "embeds": [{
                    "title": f"Neue Bewerbung ({random_title})",
                    "color": 0x5865F2,
                    "fields": [
                        {"name": "Name", "value": random_name},
                        {"name": "Alter", "value": random_age},
                        {"name": "Erfahrung", "value": random_er},
                        {"name": "Discord-Name", "value": ""},
                        {"name": "Minecraft Name", "value": ""},
                        {"name": "Minecraft Version", "value": random_version},
                        {"name": "Warum möchtest du mitarbeiten?", "value": ""}
                    ]
                }]
            }
            response = requests.post(WEBHOOK_URL, json=payload)

        if 200 <= response.status_code < 300:
            print("Erfolgreich gesendet!" + f" Request: {test} | {test2}")
        else:
            err = json.loads(response.text)
            timeout_add = round(random.uniform(0.0, 0.5), 3)
            retry_after = err.get("retry_after", 0)
            print(f"Fehler: {response.status_code} - {response.text} - Request: {test} - retry_after: {retry_after} - additonal Timeout: {timeout_add} - Sleeptime: {retry_after + timeout_add}")
            time.sleep(retry_after + timeout_add)
            test = test - 1

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Netzwerkfehler: {e}")

    test = test + 1
