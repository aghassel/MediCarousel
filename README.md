# Medicarosuel  - Utra Hacks 2024 
Shashank Ojha , ......

**Portable voice-activated surgical assistant to address surgical delays, staff shortages, and infection risks, in all public hospitals and in the front line.**

# Table of Contents
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Pitch](#pitch)
  - [Voice-Activated Control in Surgical Settings](#voice-activated-control-in-surgical-settings)
  - [Advances in Computer Vision for Surgical Safety](#advances-in-computer-vision-for-surgical-safety)
  - [Operational Benefits and Patient Care Improvements](#operational-benefits-and-patient-care-improvements)
- [Logistics & Scalability](#logistics--scalability)
- [Competitor Analysis](#competitor-analysis)
- [Software and Hardware Specifications](#software-and-hardware-specifications)
  - [Hardware Spec - Prototype](#hardware-spec---prototype)
  - [Hardware Spec - Real life](#hardware-spec---real-life)
  - [Software Spec - Product](#software-spec---product)
  - [Software Spec - Real life](#software-spec---real-life)
- [Conclusion and Future Outlook](#conclusion-and-future-outlook)

## Introduction
Medicarasouel is....

## Problem Statement

The global challenges in healthcare take on a new level of urgency. The escalating demand for healthcare services worldwide has already stretched the capacity of public health services, with 90% reporting being overwhelmed. In places like Ontario, the underutilization of hospitals due to staffing shortages, particularly among nurses, highlights the widespread nature of these challenges. Additionally, the rise in surgical delays and the alarming rate of post-surgical infections, as indicated by the WHO's report of 11% in low- to middle-income countries, underlining the need for improvement in surgical procedures and hospital efficiency.

However, these issues become even more critical in the war-torn regions of Ukraine. The main problem that needs urgent attention is the provision of sterile tools and automated assistance in surgeries on the front lines. In an environment where healthcare facilities are severely damaged or destroyed, as seen with nearly one in ten Ukrainian hospitals impacted, the ability to perform safe and effective surgeries is severely compromised. The goal is to ensure that medical practitioners in these conflict zones have access to sterile surgical tools and automated systems to aid in procedures, a necessity for addressing the immediate and pressing healthcare needs in these areas. This approach not only addresses the unique challenges posed by the war but also sets a precedent for handling similar crises in healthcare globally.

## Pitch
We are excited to present MediCarousel, a revolutionary voice-activated surgical assistant designed to enhance surgical efficiency and sterilization. MediCarousel responds to the surgeon's voice commands to provide sterilized instruments instantly, tackling two main problems in the current healthcare system: understaffing and the risk of improper sanitization tools. 

This innovation not only maintains a higher standard of sterility but also optimizes the role of scrub nurses. With MediCarousel handling instrument delivery, scrub nurses can shift their focus to more critical tasks, such as monitoring patient vitals, or be redeployed to other vital areas like post-operative care units and intensive care units.
MediCarousel: Redefining Surgical Instrument Management through Advanced Technology

The primary benefit of MediCarousel lies in its capacity to allow surgeons to select and manipulate instruments through voice commands, thereby not only optimizing the surgical process but also maintaining a critical sterile environment. 

Furthermore, the incorporation of computer vision technology ensures the organization of surgical tools, thereby elevating the standards of safety within the operating room. 

### Voice-Activated Control in Surgical Settings
Studies have shown the reduction in physical contact with instruments during surgery has been linked to a decrease in the rate of surgical site infections (SSIs), with one study reporting a 15% reduction in SSIs (Johnson & Lee, 2024). This is particularly crucial in complex surgeries where the risk of infection is higher.

Moreover, the use of voice commands in surgery fosters a more streamlined and organized operating room. The ability to instantly call upon the needed instrument reduces the time and potential errors associated with manual selection. 

### Advances in Computer Vision for Surgical Safety
Furthermore, vision contributes significantly to the organization of surgical instruments. By automatically identifying and cataloging each tool, computer vision aids in maintaining an orderly and efficient operating room. Research indicates that this level of organization can decrease the time spent on instrument preparation and handling by up to 30%, thereby reducing overall surgical time (Williams & Patel, 2024).

In summary, the incorporation of computer vision technology in surgical environments significantly bolsters surgical safety. 

## Competitor Analysis
To help the public get the best treatment they can, MediCarousal hopes to pioneer and lead a new change in the medical industry by merging the available technology in the fields of robotics and AI. Currently, many of the competitors offer a variety of robot-assisted surgical systems, assisting the surgeon in certain surgeries depending on the product type, like the Da Vinci Surgical System, used in general laparoscopic surgery. However, the majority of these systems are not only very large in size, requiring a lot of space, but also have costs ranging upwards from five hundred thousand to 2.5 million dollars, excluding the cost of operating and maintaining the system alone. This will become a huge limiting factor for many public service hospitals, especially those in third-world countries, who may not be able to afford the costs of buying and maintaining these systems. On the other hand, MediCarausol is not only considerably less expensive than these systems, it is also much easier to maintain, troubleshoot, and transport, which will make it much more accessible to all the healthcare institutions in the world, including third-world countries.

### Logistics & Scalability
After presenting the project in the hackathon, using the feedback from the judges, we will test and integrate new changes and improvements, before creating the first prototype using 3D printing. After various tests of different prototype models, we will approach medical professionals to discuss the results of the prototype. After multiple meetings, discussions and in-lab trials, we will create the final model, having integrated all the feedback and improvements from the professionals and results of the trials. This model will be delivered to various healthcare institutes and places in need through a frontline delivery and begin being executed throughout various sites, leading into international hospital implementation and execution. The expected time frame would be from January 2024 to September 2024, but may change based on further trial and testing.

## Software and Hardware Specifications
![alt text](https://github.com/aghassel/utrahacks/blob/main/images/Build.jpg?raw=True)

### Hardware Spec Prototype
Arduino Uno
IR Sensor
DC Motor
Motor driver
Battery
Raspberry Pi 4b + Camera
Carboard Structural Mounts

### Hardware Spec Real-life
![alt text](https://github.com/aghassel/utrahacks/blob/main/images/CAD_1.png?raw=True)
![alt text](https://github.com/aghassel/utrahacks/blob/main/images/CAD_2.png?raw=True)
![alt text](https://github.com/aghassel/utrahacks/blob/main/images/CAD_3.png?raw=True)

The theoretical design would consist of several mechanisms to optimize mechanical efficiency and ensure sterility. This entire mechanism would fit in a 12 cubic inch volume.

**Steam Sterilizer**: 
The Steam Sterlizer, would consist of a prefilled water deposit, or be directly connected to a supply.  This is the most common and preferred method for sterilizing surgical instruments, especially those made of stainless steel and other heat-resistant materials. It's effective against all types of microorganisms, including spores. They would be released via a high pressure and exhaust at around 134 degrees Celsius. The excess residue would be released through the chamfered vents, and cool water would be released to cool the tool. 

**Camera & Piston**:
Once the camera detects a tool the piston will be activated to make the tool to be accessible to the surgeon.

**Gears**: 
The planetary gear system with the 8:30 gear ratio for torque ensures that the servo has enough torque to push any tool while also maintaining an optimal speed of around 60 rpm (using a 200 rpm motor).

**Adjustable plate**:
The adjustable plate is a movable plate that contains all items of the device. 

### Software Spec Product
**Voice Automation**:
A wake word was created using picovoice through their porcupine API. After the wake word is detected, the following few seconds of audio are recorded, inputting the recording into the Whisper through the OpenAI API for transcription. This output is passed into the device to determine the rotation.

**Computer Vision**:
After capturing the image and transferring it to a laptop server, the image is passed into the GPT-Vision API. The output is passed into Whisper for text-to-speech functionality, outputting audio instructions.


## Conclusion and Future Outlook
MediCarousel is pioneering steps in hospital efficiency and optimization with an overall goal of providing better healthcare to the world. Our team would wish to continue this project beyond this hackathon and implement it to help improve our healthcare system with the following timeline: 


While refining the prototype we wish to work towards finishing the incorporation [consult with abdellah]...
 
In conclusion, MediCarousel is not just a testament to current technological capabilities but a beacon for future innovations in the surgical field. As we step forward into this new era, the integration of such advanced systems is poised to redefine the boundaries of what is possible in surgical precision and patient care.


