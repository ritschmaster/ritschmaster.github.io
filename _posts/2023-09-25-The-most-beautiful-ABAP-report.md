---

layout: post

title: The most beautiful ABAP report

author: Richard Bäck

---

## Introduction

Writing ABAP reports is actually very easy. For me it is so easy that the main task of writing an ABAP report is just to find out differences to ABAP reports that I have already written so that I can copy as much as possible.

In most cases this is sufficient as ABAP reports are often only for presenting data that would otherwise be hard to select. Or to have a new interface to the master/transactional data of the system but with the actual business logic hidden away in some ABAP classes. This leaves the ABAP report itself with only the task of the VC of MVC. The V(iew) can be very easily copied since most of the time it is created either by using the Dynpro painter or creating an ALV. The latter can be copied. The C(ontrol) cannot be copied since this is most likely different to each report but the cool thing is that the entire infrastructure to actually be able to implement C can be copied (e.g. subroutines etc).

But now comes the hardest part: being consistent. I have written like 20 unique ABAP reports until now. They range from only output to full user interaction. But each single one of them has its owns design constraints. For a healthy human being those differences might not even be recognizable but for me such tiny inconsistencies are hurting. My is always to make my stuff better. Getting consistent at the stuff that I am doing is a very important pillar as consistency frees up important brain resources for yet unknown stuff.

## The specification of the example report

The example report I am pasting here is about updating the material description of multiple materials using an ALV. Yes, I know that this can be achieved using the transaction *MM17*. But updating the material descriptions is very easy to understand and can be easily taken as a starting point for anything else. It can even be used as a template to implement something like a material description generation (e.g. by using [bRobots](https://www.brobots.info)).

The selection screen will consist of the following:
1. Material number selection

On execution the screen to modify the material descriptions of the selected materials will be loaded and displayed. The screen itself consists only of one ALV with the following columns:
1. Material number
    1. Read only
2. Language
    1. Read only
3. Material description
    1. Editable

After modifying the material descriptions it is possible to save the material descriptions. If the user ticked the test run option before than the materials will not be actually updated. In any case a new screen will be displayed containing messages again as ALV if the update of the materials was possible or not.

## Design constraints

To get consistency across the different reports the following design constraints have been applied:

1. Each subroutine must be treated as a pure function per default. In some cases global data must be modified but if so, then it must be declared explicitly in a header comment to the subroutine. The benefits:
    1. It makes it way easier to debug the subroutines as many subroutine can be re-executed by using the *Go to statement* feature of the ABAP debugger and just initializing the subroutine arguments within the caller of the subroutine.
    2. Reading the subroutines is easier as the reader is not required to continuously consider the global context too.
    3. Modifying global data is not hidden but directly presented to the reader.
    4. Writing pure functions normally pressures the developer in writing smaller subroutines. This makes it easier later on if new functionality has to be added as the components are better separated.
2. Subroutine parameters of the type *CHANGING* are not considered as *CHANGING* by default. Instead they are treated like *EXPORTING* of function modules. The parameter type *CHANGING* is still allowed but must be specifically declared in the comment header of the subroutine.
    1. This makes it far easier to use the feature "Go to statement" in the ABAP Debugger to re-run a specific part of the source code.
    2. Re-using subroutines is easier as *CHANGING* normally leads to writing subroutines specific to only one single use case whilst *EXPORTING* is normally implemented more generally. This hypothesis is supported by the fact that *CHANGING* can already expect certain data in a certain way.
3. Dynpro modules must not have any logic in them. Instead they must immediately call subroutines.
    1. Dynpro modules are actually global code in ABAP. Therefore it is not possible to define a variable in two modules with the same name.
    2. The modules must use the Dynpro number as a prefix.
    3. The subroutine for the module must use the Dynpro number as a prefix.
4. Global data and constants are specifically necessary for a Dynpro must use that Dynpro's number as a prefix.
5. The *START-OF-SELECTION* part and the Dynpro modules are the only code sections that are intentionally using global data. But the use of global data is immediately mitigated by passing it as argument to an according subroutine .
    1. This greatly decreases the matches of where-used lists on global data which in turn makes it easier to find where stuff happens (e.g. find out where the global data is actually modified instead of read).
6. Every include receives the prefix of the report itself followed by the following suffixes:
    1. *TXX* for a top-Include where *XX* is a serial number
        1. *T01* is reserved for global data for the entire report
        2. Each Dynpro receives its own top-include
    2. *SXX* for a selection screen where *XX* is a serial number
    3. *CXX* for a class definition **and** definition where *XX* is a serial number. The class declaration must be placed in the report's top-include as deferred.
    4. *FXX* for subroutines where *XX* is a serial number.
        1. You are free on how many includes you define but I recommend doing one for the report itself and one for each Dynpro.
    5. *OXX* for PBO modules where *XX* is a serial number.
        1. Each Dynpro receives its own PBO include
    6. *IXX* for PAI modules where *XX* is a serial number.
        1. Each Dynpro receives its own PAI include
    7. Each include's description must start with the report's name and the sequence ' - ' followed by a short description.
        1. The suffix for the include of PBO modules must be 'PBO of Dynpro XXXX' where *XXXX* is the Dynpro number
        2. The suffix for the include of PAI modules must be 'PAI of Dynpro XXXX' where *XXXX* is the Dynpro number
        3. If my recommendation is followed to separate the subroutines for each Dynpro in an include, then such include's suffix must be 'Subroutines of Dynpro XXXX' where *XXXX* is the Dynpro number.

## The implementation

With the design constraints in place we can actually start writing the example report.

The sub sections of this section are for each include necessary in the final report. As the source file is linked within the sub section only important portions are listed within this blog entry. The link to the entire report can be found in the [Appendix](#appendix).

### The report

1. See file [ZBR_MAKT_UPDATE.abap](https://raw.githubusercontent.com/ritschmaster/ritschmaster.github.io/master/assets/2023-09-30-The-most-beautiful-ABAP-Report/implementation/ZBR_MAKT_UPDATE.abap)
2. The description of the file is *ZBR: Update material descriptions*

The purpose of the report itself is mainly only to hold all the necessary includes. The only really important thing happening in here is the call to the *main* subroutine:

    * ...
    
    START-OF-SELECTION.
      PERFORM main USING s_matnr[].

As it is vital to avoid using global data the range table holding the user selected material numbers is passed in to the *main* subroutine instead of the *main* subroutine accessing it on its own directly.

### The global top include

1. See file [ZBR_MAKT_UPDATE_T01.abap](https://raw.githubusercontent.com/ritschmaster/ritschmaster.github.io/master/assets/2023-09-30-The-most-beautiful-ABAP-Report/implementation/ZBR_MAKT_UPDATE_T01.abap)
2. The description of the file is *ZBR_MAKT_UPDATE: Top-include of entire report*

The global top include actually does not store anything in this example report as there is nothing to be shared globally across the business functionality and the Dynpros. If you are relying on general constants for your business logic then you might place them in here.

### The selection include

1. See file [ZBR_MAKT_UPDATE_T02.abap](https://raw.githubusercontent.com/ritschmaster/ritschmaster.github.io/master/assets/2023-09-30-The-most-beautiful-ABAP-Report/implementation/ZBR_MAKT_UPDATE_T02.abap)
2. The description of the file is *ZBR_MAKT_UPDATE: Top-include of selection screen*

Since we only need an input field for a range of material numbers this include is again very small. The important contents are:

    * ...
    
    SELECTION-SCREEN BEGIN OF BLOCK bl1 WITH FRAME TITLE TEXT-bl1.
    
    SELECT-OPTIONS: s_matnr FOR gs_mara-matnr MODIF ID bl1.
    
    SELECTION-SCREEN END OF BLOCK bl1.

## The global subroutine include

1. See file [ZBR_MAKT_UPDATE_F01.abap](https://raw.githubusercontent.com/ritschmaster/ritschmaster.github.io/master/assets/2023-09-30-The-most-beautiful-ABAP-Report/implementation/ZBR_MAKT_UPDATE_F01.abap)
2. The description of the file is *ZBR_MAKT_UPDATE: General subroutines of the report*

In here we have only the *main* subroutine and other subroutines that are general business logic or subroutines generally necessary. Let's have a brief look at each subroutine's parameters starting with the *main* subroutine:

    * ...
    
    FORM main USING irt_matnr TYPE zbr_makt_update_rt_matnr.
    
    * ...

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/data%20dictionary/Table%20type-ZBR_MAKT_UPDATE_RT_MATNR.png?raw=true"  alt="Definition in the data dictionary of ZBR_MAKT_UPDATE_RT_MATNR" />
    <p align="center">
        Definition in the data dictionary of <i>ZBR_MAKT_UPDATE_RT_MATNR</i>
    </p>
</div> 

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/data%20dictionary/Structure-ZBR_MAKT_UPDATE_RS_MATNR.png?raw=true"  alt="Definition in the data dictionary of ZBR_MAKT_UPDATE_RS_MATNR" />
    <p align="center">
        Definition in the data dictionary of <i>ZBR_MAKT_UPDATE_RS_MATNR</i>
    </p>
</div> 

As mentioned already in section [The report](#the-report) the *main* subroutine is not accessing any global data. Instead it just operates on a selection of material numbers. Internally it then does everything necessary to load the data (model) and to start the user interface (view). For the actual implementation please have a look at the referenced source file of this section.

The loading of the data is very easy as ABAP allows us to directly access the database. It is done in the *select_data* subroutine. The model is actually only the structure *ZBR_MAKT_UPDATE_S_DATA* which is wrapped by the table type *ZBR_MAKT_UPDATE_T_DATA*.

    * ...
    
    FORM select_data USING    irt_matnr TYPE zbr_makt_update_rt_matnr
                     CHANGING et_data   TYPE zbr_makt_update_t_data.
    
    * ...

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/data%20dictionary/Structure-ZBR_MAKT_UPDATE_T_DATA.png?raw=true"  alt="Definition in the data dictionary of ZBR_MAKT_UPDATE_T_DATA" />
    <p align="center">
        Definition in the data dictionary of <i>ZBR_MAKT_UPDATE_T_DATA</i>
    </p>
</div> 

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/data%20dictionary/Structure-ZBR_MAKT_UPDATE_S_DATA.png?raw=true"  alt="Definition in the data dictionary of ZBR_MAKT_UPDATE_S_DATA" />
    <p align="center">
        Definition in the data dictionary of <i>ZBR_MAKT_UPDATE_S_DATA</i>
    </p>
</div> 

The selection itself is performed by a very simple *SELECT* statement. Here again, for the actual implementation please have a look at the referenced source file of this section.

I really encourage anyone to use this easy approach if doing stuff in ABAP. Especially if you are on your own and you do not know if there is any sophisticated approach available in the system you are placing your reports. "Why?" you may ask. Because in the most cases it just does not pay off to use anything else. Not in regard of testability as you might often can test it just right away on the development system. And especially not in regard of performance. Nothing can beat a simple *SELECT. E*xcept native HANA SQL if you want to perform fuzzy searches. Which is finally again only a hand crafted *SELECT* statement.

Only if you have to create large ABAP code bases for data transformation it makes sense to not just opt for a simple *SELECT*. In such cases I recommend outsourcing the actual selection to an implementation of the *Data Access Objects* pattern. In that way it is easier to test your code base as the actual DAOs can be easily swapped with mockup DAOs. You may find a good tutorial [here](https://blogs.sap.com/2013/03/21/abap-unit-tests-without-database-dependency-dao-concept/). The product [BRO MDM+](https://brobots.info) ships with many different DAOs already. So if you are already using BRO MDM+, then you might also opt for its DAO implementations! Just search for classes matching the pattern */HKS/CL\*DAO\**.

## The Dynpro 0100

The Dynpro 0100 is the main Dynpro of the entire report. Essentially it holds only the custom control for the eventual *CL_GUI_ALV_GRID* object stretching across the entire Dynpro area. So nothing fancy here.

The goal is to manage a table of the table type *ZBR_MAKT_UPDATE_T_DATA* with this Dynpro. Thus the final object of *CL_GUI_ALV_GRID* does not need anything special and can be modified with its available options and methods only.

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/dynpro%20setup/Dynpro_0100_01.png?raw=true"  alt="Section &quot;Attributes&quot; of the definition of Dynpro 0100" />
    <p align="center">
        Section "Attributes" of the definition of Dynpro 0100
    </p>
</div> 

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/dynpro%20setup/Dynpro_0100_02.png?raw=true"  alt="Section &quot;Element list&quot; of the definition of Dynpro 0100" />
    <p align="center">
        Section "Element list" of the definition of Dynpro 0100
    </p>
</div> 

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/dynpro%20setup/Dynpro_0100_03.png?raw=true"  alt="Section &quot;Flow logic&quot; of the definition of Dynpro 0100" />
    <p align="center">
        Section "Flow logic" of the definition of Dynpro 0100
    </p>
</div> 

## The top-include for the Dynpro 0100

1. See file [ZBR_MAKT_UPDATE_T03.abap](https://raw.githubusercontent.com/ritschmaster/ritschmaster.github.io/master/assets/2023-09-30-The-most-beautiful-ABAP-Report/implementation/ZBR_MAKT_UPDATE_T03.abap)
2. The description of the file is *ZBR_MAKT_UPDATE: Top-include of Dynpro 0100*

In here any global data needed to run the Dynpro 0100 is defined. This includes constants holding the function return codes.

## The PBO include for the Dynpro 0100

1. See file [ZBR_MAKT_UPDATE_O01.abap](https://raw.githubusercontent.com/ritschmaster/ritschmaster.github.io/master/assets/2023-09-30-The-most-beautiful-ABAP-Report/implementation/ZBR_MAKT_UPDATE_O01.abap)
2. The description of the file is *ZBR_MAKT_UPDATE: PBO of Dynpro 0100*

The PBO include holds only the modules actually used by the Dynpro. This makes the modules very small thus we can have a look at the entire include here:

    * ...
    
    MODULE 0100_init OUTPUT.
      PERFORM 0100_init CHANGING g_0100_inited
                                 gobj_0100_cc_alv
                                 gobj_0100_alv
                                 gt_0100_data_alv.
    ENDMODULE.
    
    MODULE 0100_status OUTPUT.
      PERFORM 0100_status.
    ENDMODULE.

As you can see we do not have any variable definitions or logic within the modules. Everything is handled the corresponding subroutine. But further we also avoid using any global data by passing in everything needed to actually initialize the entire Dynpro. Even the global flag *G_0100_INITED* is passed in. It holds the state if the Dynpro was already initailized and therefore must not be initialized again.

## The PAI include for the Dynpro 0100

1. See file [ZBR_MAKT_UPDATE_I01.abap](https://raw.githubusercontent.com/ritschmaster/ritschmaster.github.io/master/assets/2023-09-30-The-most-beautiful-ABAP-Report/implementation/ZBR_MAKT_UPDATE_I01.abap)
2. The description of the file is *ZBR_MAKT_UPDATE: PAI of Dynpro 0100*

As expected the modules in here are again only to act as glue code between the Dynpro and the actual ABAP subroutine. Therefore we can have a look at essentially the entire include here too:

    * ...
    
    MODULE 0100_user_command INPUT.
      PERFORM 0100_user_command USING g_0100_okcode
                                      gobj_0100_alv
                                      gt_0100_data_alv.
    ENDMODULE.

## The subroutine include for the Dynpro 0100

1. See file [ZBR_MAKT_UPDATE_F02.abap](https://raw.githubusercontent.com/ritschmaster/ritschmaster.github.io/master/assets/2023-09-30-The-most-beautiful-ABAP-Report/implementation/ZBR_MAKT_UPDATE_F02.abap)
2. The description of the file is *ZBR_MAKT_UPDATE: Subroutines of Dynpro 0100*

In here are all subroutines used by the modules and all utility subroutines for those subroutines. But business logic is completely banned from here to keep a clear separation between the includes. We start looking at the subroutine *call_screen_0100*:

    * ...
    
    FORM call_screen_0100 USING it_data TYPE zbr_makt_update_t_data.
      PERFORM 0100_normal_to_alv USING it_data
                                 CHANGING gt_0100_data_alv.
    
      SORT gt_0100_data_alv BY matnr ASCENDING
                               spras ASCENDING.
    
      CALL SCREEN 0100.
    ENDFORM.
    
    * ...

This subroutine is essentially the main subroutine of the Dynrpro and wraps the *CALL SCREEN* statement. Wrapping the *CALL SCREEN* this way assures that the caller of the Dynpro is aware of the data needed and data returned. Otherwise some obscure global variable must be set/read which is most likely not documented at all.

The subroutine *0100_normal_to_alv* requires also some explanations. The report strongly separates the model data (here named *normal*) from the view data (here named *alv*). This is done in *0100_normal_to_alv*. The resulting data is then eventually consumed by the *CL_GUI_ALV_GRID*, Accordingly there is also a subroutine named *0100_alv_to_normal* to perform the conversion in the other direction.

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/data%20dictionary/Table%20type-ZBR_MAKT_UPDATE_T_DATA_ALV.png?raw=true"  alt="Definition in the data dictionary of ZBR_MAKT_UPDATE_T_DATA_ALV" />
    <p align="center">
        Definition in the data dictionary of <i>ZBR_MAKT_UPDATE_T_DATA_ALV</i>
    </p>
</div> 

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/data%20dictionary/Structure-ZBR_MAKT_UPDATE_S_DATA_ALV.png?raw=true"  alt="Definition in the data dictionary of ZBR_MAKT_UPDATE_S_DATA_ALV" />
    <p align="center">
        Definition in the data dictionary of <i>ZBR_MAKT_UPDATE_S_DATA_ALV</i>
    </p>
</div> 

Next up are the subroutines that are used by the modules:

    * ...
    
    * The parameter C_INITED defines if the Dynpro 0100 has been initialized. It
    * is a true CHANGING parameter.
    *
    * The parameter CCL_CONTAINER is a true CHANGING parameter.
    *
    * The parameter CC_ALV is a true CHANGING parameter.
    *
    * The parameter CT_DATA_ALV is a true CHANGING parameter.
    FORM 0100_init CHANGING c_inited TYPE flag
                            cobj_cc_alv TYPE REF TO cl_gui_custom_container
                            cobj_alv TYPE REF TO cl_gui_alv_grid
                            ct_data_alv TYPE zbr_makt_update_t_data_alv.
    
    * ...
    
    FORM 0100_status.
    
    * ...
    
    FORM 0100_user_command USING i_okcode TYPE syucomm
                                 iobj_alv TYPE REF TO cl_gui_alv_grid
                                 it_data_alv TYPE zbr_makt_update_t_data_alv.
    
    * ...

If you are familiar with writing ABAP reports (which I expect that you are), then you might already know what those subroutines are up to.

Finally the utility subroutines which are needed:

    * ...
    
    FORM 0100_fieldcatalog CHANGING et_fieldcatalog TYPE lvc_t_fcat.
    
    * ...
    
    FORM 0100_normal_to_alv USING it_data TYPE zbr_makt_update_t_data
                            CHANGING et_data_alv TYPE zbr_makt_update_t_data_alv.
    
    * ...
    
    FORM 0100_alv_to_normal USING it_data_alv TYPE zbr_makt_update_t_data_alv
                            CHANGING et_data TYPE zbr_makt_update_t_data.
    
    * ...
    
    * The parameter C_INITED defines if the Dynpro 0100 has been initialized. It
    * is a true CHANGING parameter.
    *
    * The parameter CCL_CONTAINER is a true CHANGING parameter.
    *
    * The parameter CC_ALV is a true CHANGING parameter.
    FORM 0100_reset CHANGING c_inited TYPE flag
                             gobj_cc_alv TYPE REF TO cl_gui_custom_container
                             gobj_alv TYPE REF TO cl_gui_alv_grid.
    
    * ...

## The Dynpro 0101

The Dynpro 0101 is a utility Dynpro. Its purpose is to list messages of the structure type *BAPIRET2* as ALV. This is really handy if many messages are shown to the user as then it is possible to easily filter them. A normal user might just use a layout with a filter showing error messages whilst a developer can have a look at all messages. This really helps over the lifespan of the report as normally the most esoteric errors show up after 1 year in production use.

One core functionality of *BAPIRET2* is to link the message text to an actual message within a message class in the current SAP system. That way it is possible to define not only a short message text which is directly presented to the user but a further long text going more into depth on what has happened. This is generally very useful to document weird use cases or errors that would otherwise be forgotten in the mists of time.

The issue at hand is now that the class *CL_GUI_ALV_GRID* does not now the data that it wraps. Thus the available options and methods are not sufficient to cover the use case of displaying a table of *BAPIRET2*. We will have to add a new column manually containing a clickable "Display more information" icon. This will be done through section [The PBO include for the Dynpro 0101](#the-pbo-include-for-the-dynpro-0101). Additionally we have to react on the click on that icon to display the long text for that message. This will be implemented by using a custom event receiver that is attached to the *CL_GUI_ALV_GRID* object of this Dynpro. The event handler is shown in section [The class include for the Dynpro 0101](#the-class-include-for-the-dynpro-0101).

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/dynpro%20setup/Dynpro_0101_01.png?raw=true"  alt="Section &quot;Attributes&quot; of the definition of Dynpro 0101" />
    <p align="center">
        Section "Attributes" of the definition of Dynpro 0101
    </p>
</div> 

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/dynpro%20setup/Dynpro_0101_02.png?raw=true"  alt="Section &quot;Element list&quot; of the definition of Dynpro 0101" />
    <p align="center">
        Section "Element list" of the definition of Dynpro 0101
    </p>
</div> 

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/dynpro%20setup/Dynpro_0101_03.png?raw=true"  alt="Section &quot;Flow logic&quot; of the definition of Dynpro 0101" />
    <p align="center">
        Section "Flow logic" of the definition of Dynpro 0101
    </p>
</div> 

## The top-include for the Dynpro 0101

1. See file [ZBR_MAKT_UPDATE_T04.abap](https://raw.githubusercontent.com/ritschmaster/ritschmaster.github.io/master/assets/2023-09-30-The-most-beautiful-ABAP-Report/implementation/ZBR_MAKT_UPDATE_T04.abap)
2. The description of the file is *ZBR_MAKT_UPDATE: Top-include of Dynpro 0101*

The same principles as in the section [The top-include for the Dynpro 0100](#the-top-include-for-the-dynpro-0100) are applied to this include.

## The class include for the Dynpro 0101

1. See file [ZBR_MAKT_UPDATE_C01.abap](https://raw.githubusercontent.com/ritschmaster/ritschmaster.github.io/master/assets/2023-09-30-The-most-beautiful-ABAP-Report/implementation/ZBR_MAKT_UPDATE_C01.abap)
2. The description of the file is *ZBR_MAKT_UPDATE: Local classes for Dynpro 0101*

As mentioned in section [The Dynpro 0101](#the-dynpro-0101) an event receiver is needed to handle the click on the "Display more information" icon. The implementation of the event receiver is done within this include.

The entire class is only a glue code to eventually call the subroutine *0101_handle_hotspot_click*. It is rather short so I list the entire source code of it:

    *...
    
    CLASS zcl_0101_alv_event_receiver DEFINITION.
      PUBLIC SECTION.
        METHODS:
          constructor
            IMPORTING
              it_0101_alv_data_ref TYPE REF TO zbr_makt_update_t_bapiret2,
              get_0101_alv_data_ref
            RETURNING
              VALUE(robj_0101_alv_data_ref) TYPE REF TO zbr_makt_update_t_bapiret2,
          handle_hotspot_click
          FOR EVENT double_click OF cl_gui_alv_grid
            IMPORTING
              e_row
              e_column
              es_row_no.
    
      PRIVATE SECTION.
        DATA:
          t_0101_alv_data_ref TYPE REF TO zbr_makt_update_t_bapiret2.
    ENDCLASS.
    
    CLASS zcl_0101_alv_event_receiver IMPLEMENTATION.
      METHOD constructor.
        t_0101_alv_data_ref = it_0101_alv_data_ref.
      ENDMETHOD.
      
      METHOD get_0101_alv_data_ref.
        robj_0101_alv_data_ref = t_0101_alv_data_ref.
      ENDMETHOD.
      
      METHOD handle_hotspot_click.
        DATA(lobj_0101_alv_data_ref) = get_0101_alv_data_ref( ).
        
        PERFORM 0101_handle_hotspot_click USING e_row
                                                e_column
                                                lobj_0101_alv_data_ref.
      ENDMETHOD.
    ENDCLASS.

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/data%20dictionary/Table%20type-ZBR_MAKT_UPDATE_T_BAPIRET2.png?raw=true"  alt="Definition in the data dictionary of ZBR_MAKT_UPDATE_T_BAPIRET2" />
    <p align="center">
        Definition in the data dictionary of <i>ZBR_MAKT_UPDATE_T_BAPIRET2</i>
    </p>
</div> 

<div>
    <img src="https://github.com/ritschmaster/zbr_makt_update/blob/main/data%20dictionary/Structure-ZBR_MAKT_UPDATE_S_BAPIRET2.png?raw=true"  alt="Definition in the data dictionary of ZBR_MAKT_UPDATE_S_BAPIRET2" />
    <p align="center">
        Definition in the data dictionary of <i>ZBR_MAKT_UPDATE_S_BAPIRET2</i>
    </p>
</div> 

The really important part of this class is that the actual data of the *CL_GUI_ALV_GRID* object is again not accessed using global data. Instead a reference to the data is stored within the object of this class in the attribute *t_0101_alv_data_ref*. The above implementation will avoid the following issues:

No dangling reference for the event receiver: as the implementation of this class is very clean we can create the object of it during the initialization process of the *CL_GUI_ALV_GRID* object and forget it afterwards. The necessary reference to event receiver is hold by the *CL_GUI_ALV_GRID* object anyway. So if that gets collected by the garbage collector then the event receiver is too.

Overpopulation of the where-used list of the actual data of the ALV: The actual global variable is not used in here. This is great as a later developer debugging the report is normally not interested in finding this class or its implementation at that stage.

## The PBO include for the Dynpro 0101

1. See file [ZBR_MAKT_UPDATE_O02.abap](https://raw.githubusercontent.com/ritschmaster/ritschmaster.github.io/master/assets/2023-09-30-The-most-beautiful-ABAP-Report/implementation/ZBR_MAKT_UPDATE_O02.abap)
2. The description of the file is *ZBR_MAKT_UPDATE: PBO of Dynpro 0101*

The PBO modules here are looking very similar to the ones already seen in [The PBO include for the Dynpro 0100](#the-pbo-include-for-the-dynpro-0100). I will skip any explanation of it.

## The PAI include for the Dynpro 0101

1. See file [ZBR_MAKT_UPDATE_I02.abap](https://raw.githubusercontent.com/ritschmaster/ritschmaster.github.io/master/assets/2023-09-30-The-most-beautiful-ABAP-Report/implementation/ZBR_MAKT_UPDATE_I02.abap)
2. The description of the file is *ZBR_MAKT_UPDATE: PAI of Dynpro 0101*

The PAI modules here are looking very similar to the ones already seen in [The PAI include for the Dynpro 0100](#the-pai-include-for-the-dynpro-0100). I will skip any explanation of it.

## The subroutine include for the Dynpro 0101

1. See file [ZBR_MAKT_UPDATE_F03.abap](https://raw.githubusercontent.com/ritschmaster/ritschmaster.github.io/master/assets/2023-09-30-The-most-beautiful-ABAP-Report/implementation/ZBR_MAKT_UPDATE_F03.abap)
2. The description of the file is *ZBR_MAKT_UPDATE: Subroutines of Dynpro 0101*

The subroutines are mostly looking similar to the ones already seen in [The subroutine include for the Dynpro 0100](#the-subroutine-include-for-the-dynpro-0100).The most interesting parts are:

The model data and the view data do not differ in the implementation. This is actually not quite correct as the model data does actually differ from the view data. The attribute *STATUS* which contains the eventually clickable icon should is irrelevant for the model. But to keep it simple I have skipped separating the model data from the view data.

The subroutine *call_screen_0101* actually uses *BAPIRET2_T* directly to interface with the caller.

The setup of the event receiver which is done in the subroutine *0101_init*.

The handling of the click on the "Display more information" icon which is done in the subroutine *0101_handle_hotspot_click*.

Here are the interesting parts of those subroutines:

    * ...
    
    *FORM call_screen_0101 USING it_data TYPE bapiret2_t.*
    
    * ...
    
    * The parameter C_INITED defines if the Dynpro 0101 has been initialized. It
    * is a true CHANGING parameter.
    *
    * The parameter CCL_CONTAINER is a true CHANGING parameter.
    *
    * The parameter CC_ALV is a true CHANGING parameter.
    *
    * The parameter CT_DATA_ALV is a true CHANGING parameter.
    FORM 0101_init CHANGING c_inited TYPE flag
                            cobj_cc_alv TYPE REF TO cl_gui_custom_container
                            cobj_alv TYPE REF TO cl_gui_alv_grid
                            ct_data_alv TYPE zbr_makt_update_t_bapiret2.
    
    * ... Not interesting parts of 0101_init ...
    
    "============================================================================
    " Setup the handlers of COBJ_ALV
    
    DATA: ct_data_alv_ref TYPE REF TO zbr_makt_update_t_bapiret2.
    GET REFERENCE OF ct_data_alv INTO ct_data_alv_ref.
    
    DATA: lobj_event_receiver TYPE REF TO zcl_0101_alv_event_receiver.
    lobj_event_receiver = NEW zcl_0101_alv_event_receiver(
      it_0101_alv_data_ref = ct_data_alv_ref
    ).
    
    SET HANDLER lobj_event_receiver-\>handle_hotspot_click FOR cobj_alv.
    
    "============================================================================
    " Setup the actual ALV object GOBJ_ALV
    CALL METHOD cobj_alv-\>set_table_for_first_display
      EXPORTING
        is_variant = ls_variant
        is_layout = ls_layout
        i_save = abap_true
        it_toolbar_excluding = lt_toolbar_excluding
      CHANGING
        it_fieldcatalog = lt_fieldcatalog
        it_sort = lt_sort
        it_outtab = ct_data_alv.
    
    "============================================================================
    " Set the Dynpro to be initialized
    c_inited = abap_true.
    ENDFORM.
    
    * ...
    
    FORM 0101_handle_hotspot_click USING i_row TYPE lvc_s_row
                                         i_column TYPE lvc_s_col
                                         it_data_alv TYPE REF TO zbr_makt_update_t_bapiret2.
    
    "============================================================================
    " Get the row the user clicked into <IS_DATA_ALV>
    FIELD-SYMBOLS: <it_data_alv> TYPE zbr_makt_update_t_bapiret2.
    ASSIGN it_data_alv->* TO <it_data_alv>.
    READ TABLE <it_data_alv> ASSIGNING FIELD-SYMBOL(<is_data_alv>) INDEX i_row-index.
    
    "============================================================================
    " Exit out if the index could not be assigned
    IF sy-subrc <> 0.
      RETURN.
    ENDIF.
    
    "============================================================================
    " Get the key of the message
    DATA: lf_dokname TYPE string.
    CONCATENATE <is_data_alv>-id <is_data_alv>-number INTO lf_dokname.
    
    "============================================================================
    " Show the longtext of the message
    DATA: lt_link TYPE TABLE OF tline.
    CALL FUNCTION 'HELP_OBJECT_SHOW'
      EXPORTING
        dokclass = 'NA'
        doklangu = sy-langu
        dokname = lf_dokname
        msg_var_1 = <is_data_alv>-message_v1
        msg_var_2 = <is_data_alv>-message_v2
        msg_var_3 = <is_data_alv>-message_v3
        msg_var_4 = <is_data_alv>-message_v4
      TABLES
        links = lt_link
      EXCEPTIONS
        object_not_found = 1
        sapscript_error = 2
        OTHERS = 3.
    ENDFORM.
    
    * ...

## Conclusion

I hope that I managed to present the idea in an understandable way to you, dear reader. If not, please do not hesitate to send me an e-mail with ideas on how to enhance this blog entry.

As mentioned in the introduction already this is my latest approach to write ABAP reports. Currently I am not aware of any ways to improve it. But most likely there are still gaps to be closed.

Nevertheless I have already successfully used the ideas of this blog entry in many projects. Each time it helped not only me but also my colleagues to get faster into the project's implementation.

## Appendix

The entire report is available under MIT license [here](https://github.com/ritschmaster/zbr_makt_update). That repository also lists any missing data dictionary definitions needed to get the entire report up and running.
