---

layout: post

title: Using BRO for mass-creation of materials

author: Richard Bäck

---

Since I am an ABAP developer and I am also using [BRO](https://brobots.info) since 2017 - I want to show off a great capability of BRO: easily creating many materials in SAP at once with arbitrary data. The cool parts:

1. It can use calculation logics. This makes it way more powerful then the transaction *MM17* - which only takes the final values for the database tables of a material.
2. No ABAP logic is necessary.

But first off: what is BRO? BRO stands for Business Rules Organizer and is a paid SAP ERP addon allowing creating business rules. The rules themselves are organized in a completely different way than its direct competitor BRF+ (Business Rules Framework+) which is an official module within SAP ERP. The organization of rules is actually really unique. A rule consists of steps which itself consists of conditions and actions. The unique part is that the actions:

1. allow calling other rules which are then in turn executed.
2. allow calling function modules and thus arbitrary Z-code.
3. are using action types which allow custom implementations in ABAP too.

tl;dr a BRO rule is a subroutine containing a big IF-ELSE.

This features allows a seamless switch between actual business rules (containing only data) and low-level stuff like saving a material.

<div>
    <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image1.png"  alt="A rule with some conditions and actions" />
    <p align="center">
        A rule with some conditions and actions
    </p>
</div> 

## Prerequisites

1. Basic knowledge on BRO.
2. Since you are most likely a BRO user already, please make sure that you are running at least BRO 5.4.3 with its default customizing.
3. You are running the latest material low-level rules of the *bRobots MDM+ Material* decision area that are available for BRO 5.4.3.
    1. To check this, check if the rule *BMAP\_BAPIE1MARA\_MAPPED* is available.
4. Basic knowledge on the database tables for materials in SAP. E.g. MARA, MARC

## The goal

The goal is to easily create multiple commodities at once with only a minimum of basic data and a single material description in English.

## Setup

### Creating the rule

The start rule will be one material per step. This will allow us to have an easy view on the materials to be created. We can create the new rule by simply doing the following:

1.  Right click on the category *90.* (The category might be named with the name of your company) and click *Create new rule*
    <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image2.png" />
2.  Use the name *DEMO\_MASS* for the new rule and hit *Enter*.
    1.  Rule names are not case sensitive and will always be converted to upper case.  
        <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image3.png" />
3.  Now set the data on the rule header  
    <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image4.png" />
    1.  Use *Multi-hit* as the *Rule type*. This is necessary to execute **all** steps from top to bottom if their condition apply.
        1.  *Single-hit* will exit after the first step has been executed.
    2.  It is a good practise to indicate a user group responsible for the rule by setting an *Authority group*. In my case I can use *ADMIN*.

### Adding the boilerplate code

You are now sitting in front of a new empty rule. You may already be able to fill *MARA* fields. But doing so right away will not lead to any results. Setting *MARA* fields alone will not result in creating a material. Since BRO will only do what it is told to do nothing will be done other than setting some fields during the runtime execution.

To actually create a material some boilerplate code is needed. Some special function modules must be called in a sequence. The first one being a function module to actually perform the material creation. The second one to commit the material to the database. So we will need the following function modules:

1.  ***/HKS/BRO\_MDM\_AC\_MATERIAL***
2.  */HKS/BRO\_MDM\_AC\_COMMIT\_WORK*
    1.  For testing purposes we use */HKS/BRO\_MDM\_AC\_ROLLBACK\_WORK* for now. This will undo the changes scheduled by */HKS/BRO\_MDM\_AC\_MATERIAL* instead of committing them to the database.

So our first version might look like the following:

<img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image5.png" />

But this will not work at all (again). Those function modules are not to be called directly. They are somewhat magic function modules which are collected and executed automatically in sequence. Such automatically executed function modules are called **action function module**.

So to actually get it up and working correctly we have to use a function module which consumes the action function modules and is really executed right away. This function module is called */HKS/BRO\_MDM\_PROCESS\_ACTION\_FM*. Adding this one will result in the following rule:

<img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image6.png"  />

Additionally I have added two new variables:

1.  *SV\_HKS\_IMMEDIATE = C\_YES*
    1.  This will register action function modules that are stated after this statement for the function module */HKS/BRO\_MDM\_PROCESS\_ACTION\_FM*.
2.  *SV\_ADD\_BRO\_MSG = C\_YES*
    1.  This will result in outputting any error and success messages created by the action function modules

### First test run

It is already possible to successfully execute the rule. But it will not result in doing anything at all. It does not even try to create materials - which should make sense to you since we have not stated any material data yet.

The rule can be executed without any inputs. The rule will remain not relying on any inputs as everything needed by the main action function module */HKS/BRO\_MDM\_AC\_MATERIAL* will be stated within the rule anyway.

You may now execute the rule to check if it does not lead to a system dump. 😊

<div>
    <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image7.png" alt="Results of the first test run - nothing at all" />
    <p align="center">
        Results of the first test run - nothing at all
    </p>
</div>

## Adding the boilerplate code II

Before we can finally start stating material data we have to add some remaining boiler plate code. To explain why we are using the upcoming boilerplate code we have to first understand what the action function module */HKS/BRO\_MDM\_AC\_MATERIAL* is taking as inputs. Said action function module is using structures starting with *BAPIE1* as inputs. The most important one is *BAPIE1MARA* which holds the - as you might already suspect - general data of the material. But please do not fall for the idea that this is straight forward. *BAPIE1MARA* is not the same as the database table MARA. The difference are the names of the attributes which are abbreviations in English (e.g. *BAPIE1MARA-MATL\_GROUP* which is applied to *MARA-MATKL*). But there are also some more minor differences.

<div>
    <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image8.png" alt="The first part of the structure BAPIE1MARA" />
    <p align="center">
        The first part of the structure BAPIE1MARA
    </p>
</div>

This comes with the following down sides:

1.  Necessary fields cannot just be determined by using the technical view within the F1 help for a field in *MM01*/*MM02*/*MM03*
2.  The structure of the BAPI must be known and translated to what one want to actually achieve.

So to avoid those downsides we use an abstraction layer. This abstraction layer is called ***BAPI Mapping*** and is responsible for translating *MARA* fields to *BAPIE1MARA* fields and so on. *BAPI Mapping* is actually a 3 staged process:

1.  State once which fields should be updated (for a creation all fields should be updated). Stating to update all fields is as easy as calling the rule *BMAP\_BAPIE1MARA\_BAPI\_FIELDS*.
2.  Move an entire *MARA* line into an internal buffer after the *MARA* line has been fully described. This is as easy as calling the rule *BMAP\_BAPIE1MARA\_MAPPED*.
3.  After the last *MARA* line has been moved, the entire buffer has been processed to make it available for the action function module */HKS/BRO\_MDM\_AC\_MATERIAL*. This is as easy as calling the rule *BMAP\_BAPIE1*.

For the sake of simplicity I have only considered the database table *MARA* in the last enumeration. But you may just substitute the name *MARA* with the database table you want to describe (i.e. *MARC*). Just keep in mind to keep the order and that the 3<sup>rd</sup> step must be done only once. The 1<sup>st</sup> step can be done for each line individually but in most cases the same attributes of all lines have to be updated and thus the rule is called only once.

Now to finish this chapter we just place the rules *BMAP\_BAPIE1MARA\_BAPI\_FIELDS* and *BMAP\_BAPIE1* at start of the rule.

<div>
    <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image9.png" alt="The rule with the remaining boilerplate code only" />
    <p align="center">
        The rule with the remaining boilerplate code only
    </p>
</div>

You may again execute the rule. But yet again nothing will happen.

Since we might add many materials it comes in quite helpful to outsource the description of the material fields in some other rule. Therefore we create a new rule called *DEMO\_MASS\_DATA* and place it between the new added steps.

<div>
    <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image10.png" alt="Updated main rule outsourcing the material data" />
    <p align="center">
        Updated main rule outsourcing the material data
    </p>
</div>

<div>
    <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image11.png" alt="New rule carrying the actual material data to be created" />
    <p align="center">
        New rule carrying the actual material data to be created
    </p>
</div>

## Adding the data

### The header line

Now finally we can add the data. But before we do so we think of a nice structure to ensure that the table is actually readable by fellow human beings. First we think of the attributes we need:

1.  The material number
    1.  A must as otherwise we cannot identify the material
    2.  For simplicity I expect you to use an external number range
1.  The industry sector
    1.  A required field by the SAP standard
2.  The material type
    1.  A required field by the SAP standard
3.  The material group
    1.  A required field by the SAP standard
4.  The base unit of measurement
    1.  A required field by the SAP standard
5.  The material description
    1.  Not required by the SAP standard but it makes sense to state it
6.  The language of the material description
    1.  Required by SAP as the material description is translatable

The material must supplied twice - unfortunately. A second time for the material description as the table *MAKT* also needs it.

Rotate this enumeration by 90 degrees and you have table headers. I place those table headers as comment line within the rule as reference into the rule. But you will see that you will not need that header at all later on.

<div>
    <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image12.png" alt="The data carrying rule with only the header line" />
    <p align="center">
        The data carrying rule with only the header line
    </p>
</div>

### The data

Alright, with this good looking header rule we can actually place some lines in there.

<div>
    <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image13.png" alt="The data carrying rule with some data" />
    <p align="center">
        The data carrying rule with some data
    </p>
</div>

On the data itself: it must be written fully in the internal SAP format. On the base unit of measurement: the cause for using *ST* instead of *PC* for piece is that SAP internally uses the value *ST*. This is also the same cause for supplying leading zeroes for the material number.

If you are a careful reader, then you might ask yourself now why I am not using the rule *BMAP\_BAPIE1MARA\_MAPPED*. The answer is: I just wanted to explain the basic idea without some weird looking functional rules this actually looks like a good ol’ Excel sheet.

So now we can place the following rule calls at the end of each line:

1.  *BMAP\_BAPIE1MATHEADER\_MAPPED*
    1.  This is a special rule which is needed in tandem with *BMAP\_BAPIE1MARA\_MAPPED* to indicate which material views (in the sense of *MM01*) should be created.
    2.  This rule will create the maximum available material views for the selected material type.
2.  *BMAP\_BAPIE1MARA\_MAPPED*
3.  *BMAP\_BAPIE1MAKT\_MAPPED*

<div>
    <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image14.png" alt="The data carrying rule fully functional" />
    <p align="center">
        The data carrying rule fully functional
    </p>
</div>

### First actual test run

Now we can finally execute the rule DEMO\_MASS and actually receive some meaningful outputs. To get the output messages you have to scroll down to the bottom in the table *Processing steps* and check the column *Msg. changed*. Double clicking its cell will present me the 3 success messages - one for each new material.

<div>
    <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image15.png" alt="First actual test run creating materials" />
    <p align="center">
        First actual test run creating materials
    </p>
</div>

An important note: we are still rolling back the changes. So we can execute this rule as long as we want. Knowing this you can now play around with the data as much as you want. You can even explore further tables like the plant specific data (*MARC*) in which you are most likely interested.

## Production run

To switch to a production run you have to simply swap the action function module */HKS/BRO\_MDM\_AC\_ROLLBACK\_WORK* with */HKS/BRO\_MDM\_AC\_COMMIT\_WORK* in the main rule. Running the rule afterwards will commit the created materials to the database and they are available in the transaction *MM03* and so on immediately afterwards.

<div>
    <img src="/assets/2023-05-01-Using-BRO-for-mass-creation-of-materials/image16.png" alt="The main rule updated to be ready for a production run" />
    <p align="center">
        The main rule updated to be ready for a production run
    </p>
</div>

## Bonus: updating materials

Now that we know how to create materials - wouldn’t it be wonderful if we could update materials too? Especially if the production run was not tested well enough, this could come in very hand.

Luckily this is as easy as re-running the production run. Why? Because the action function module */HKS/BRO\_MDM\_AC\_MATERIAL* does not care whether the material exists or not. If it does not exist, then it is created. If it does exist, then it will just be updated.

So just make sure that you are not creating more materials then needed and you should be safe even with not well enough defined data.
