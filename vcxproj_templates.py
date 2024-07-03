import os

def get_vcxproj_content(project_name):
    return f'''<?xml version="1.0" encoding="utf-8"?>
<Project DefaultTargets="Build" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <ItemGroup Label="ProjectConfigurations">
    <ProjectConfiguration Include="Debug|x64">
      <Configuration>Debug</Configuration>
      <Platform>x64</Platform>
    </ProjectConfiguration>
    <ProjectConfiguration Include="Release|x64">
      <Configuration>Release</Configuration>
      <Platform>x64</Platform>
    </ProjectConfiguration>
  </ItemGroup>
  <PropertyGroup Label="Globals">
    <ProjectGuid>{{{os.urandom(16).hex().upper()}}}</ProjectGuid>
    <RootNamespace>{project_name}</RootNamespace>
    <WindowsTargetPlatformVersion>10.0</WindowsTargetPlatformVersion>
  </PropertyGroup>
  <Import Project="$(VCTargetsPath)\\Microsoft.Cpp.Default.props" />
  <PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Debug|x64'" Label="Configuration">
    <ConfigurationType>DynamicLibrary</ConfigurationType>
    <UseDebugLibraries>true</UseDebugLibraries>
    <PlatformToolset>v143</PlatformToolset>
    <CharacterSet>Unicode</CharacterSet>
  </PropertyGroup>
  <PropertyGroup Condition="'$(Configuration)|$(Platform)'=='Release|x64'" Label="Configuration">
    <ConfigurationType>DynamicLibrary</ConfigurationType>
    <UseDebugLibraries>false</UseDebugLibraries>
    <PlatformToolset>v143</PlatformToolset>
    <WholeProgramOptimization>true</WholeProgramOptimization>
    <CharacterSet>Unicode</CharacterSet>
  </PropertyGroup>
  <Import Project="$(VCTargetsPath)\\Microsoft.Cpp.props" />
  <ImportGroup Label="ExtensionSettings" />
  <ImportGroup Label="Shared" />
  <ImportGroup Label="PropertySheets" Condition="'$(Configuration)|$(Platform)'=='Debug|x64'">
    <Import Project="$(UserRootDir)\\Microsoft.Cpp.$(Platform).user.props" Condition="exists('$(UserRootDir)\\Microsoft.Cpp.$(Platform).user.props')" Label="LocalAppDataPlatform" />
  </ImportGroup>
  <ImportGroup Label="PropertySheets" Condition="'$(Configuration)|$(Platform)'=='Release|x64'">
    <Import Project="$(UserRootDir)\\Microsoft.Cpp.$(Platform).user.props" Condition="exists('$(UserRootDir)\\Microsoft.Cpp.$(Platform).user.props')" Label="LocalAppDataPlatform" />
  </ImportGroup>
  <PropertyGroup Label="UserMacros" />
  <PropertyGroup>
    <_ProjectFileVersion>10.0.30319.1</_ProjectFileVersion>
    <OutDir>$(SolutionDir)$(Configuration)\\</OutDir>
    <IntDir>$(SolutionDir)$(Configuration)\\$(ProjectName)\\</IntDir>
    <TargetName>$(ProjectName)</TargetName>
  </PropertyGroup>
  <ItemDefinitionGroup Condition="'$(Configuration)|$(Platform)'=='Debug|x64'">
    <ClCompile>
      <WarningLevel>Level3</WarningLevel>
      <Optimization>Disabled</Optimization>
      <PreprocessorDefinitions>WIN32;_DEBUG;_WINDOWS;_USRDLL;%(PreprocessorDefinitions)</PreprocessorDefinitions>
      <RuntimeLibrary>MultiThreadedDebugDLL</RuntimeLibrary>
      <LanguageStandard>stdcppLatest</LanguageStandard>
    </ClCompile>
    <Link>
      <SubSystem>Windows</SubSystem>
      <GenerateDebugInformation>true</GenerateDebugInformation>
    </Link>
  </ItemDefinitionGroup>
  <ItemDefinitionGroup Condition="'$(Configuration)|$(Platform)'=='Release|x64'">
    <ClCompile>
      <WarningLevel>Level3</WarningLevel>
      <Optimization>MaxSpeed</Optimization>
      <FunctionLevelLinking>true</FunctionLevelLinking>
      <IntrinsicFunctions>true</IntrinsicFunctions>
      <PreprocessorDefinitions>WIN32;NDEBUG;_WINDOWS;_USRDLL;%(PreprocessorDefinitions)</PreprocessorDefinitions>
      <RuntimeLibrary>MultiThreadedDLL</RuntimeLibrary>
      <LanguageStandard>stdcppLatest</LanguageStandard>
    </ClCompile>
    <Link>
      <SubSystem>Windows</SubSystem>
      <EnableCOMDATFolding>true</EnableCOMDATFolding>
      <OptimizeReferences>true</OptimizeReferences>
      <GenerateDebugInformation>true</GenerateDebugInformation>
    </Link>
  </ItemDefinitionGroup>
  <ItemGroup>
    <ClCompile Include="Main.cpp">
      <Filter>Source Files</Filter>
    </ClCompile>
    <ClInclude Include="NameCollisions.inl">
      <Filter>Source Files</Filter>
    </ClInclude>
    <ClInclude Include="PropertyFixup.hpp">
      <Filter>Source Files</Filter>
    </ClInclude>
    <ClInclude Include="SDK.hpp">
      <Filter>Source Files</Filter>
    </ClInclude>
    <ClInclude Include="UnrealContainers.hpp">
      <Filter>Source Files</Filter>
    </ClInclude>
  </ItemGroup>
  <ItemGroup>
    <ClCompile Include="SDK\\Basic.cpp">
      <Filter>MoreFiles</Filter>
    </ClCompile>
    <ClCompile Include="SDK\\CoreUObject_functions.cpp">
      <Filter>MoreFiles</Filter>
    </ClCompile>
    <ClCompile Include="SDK\\Engine_functions.cpp">
      <Filter>MoreFiles</Filter>
    </ClCompile>
  </ItemGroup>
  <Import Project="$(VCTargetsPath)\\Microsoft.Cpp.targets" />
  <ImportGroup Label="ExtensionTargets" />
</Project>
'''

def get_vcxproj_filters_content():
    return f'''<?xml version="1.0" encoding="utf-8"?>
<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <ItemGroup>
    <Filter Include="Source Files">
      <UniqueIdentifier>{{{os.urandom(16).hex().upper()}}}</UniqueIdentifier>
      <Extensions>cpp;c;cc;cxx;def;odl;idl;hpj;bat;asm;asmx</Extensions>
    </Filter>
    <Filter Include="MoreFiles">
      <UniqueIdentifier>{{{os.urandom(16).hex().upper()}}}</UniqueIdentifier>
    </Filter>
  </ItemGroup>
  <ItemGroup>
    <ClCompile Include="Main.cpp">
      <Filter>Source Files</Filter>
    </ClCompile>
    <ClInclude Include="NameCollisions.inl">
      <Filter>Source Files</Filter>
    </ClInclude>
    <ClInclude Include="PropertyFixup.hpp">
      <Filter>Source Files</Filter>
    </ClInclude>
    <ClInclude Include="SDK.hpp">
      <Filter>Source Files</Filter>
    </ClInclude>
    <ClInclude Include="UnrealContainers.hpp">
      <Filter>Source Files</Filter>
    </ClInclude>
  </ItemGroup>
  <ItemGroup>
    <ClCompile Include="SDK\\Basic.cpp">
      <Filter>MoreFiles</Filter>
    </ClCompile>
    <ClCompile Include="SDK\\CoreUObject_functions.cpp">
      <Filter>MoreFiles</Filter>
    </ClCompile>
    <ClCompile Include="SDK\\Engine_functions.cpp">
      <Filter>MoreFiles</Filter>
    </ClCompile>
  </ItemGroup>
</Project>
'''

def get_sln_content(project_name):
    return f'''Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 17
VisualStudioVersion = 17.0.31912.275
MinimumVisualStudioVersion = 10.0.40219.1
Project("{{{os.urandom(16).hex().upper()}}}") = "{project_name}", "{project_name}.vcxproj", "{{{os.urandom(16).hex().upper()}}}"
EndProject
Global
    GlobalSection(SolutionConfigurationPlatforms) = preSolution
        Debug|x64 = Debug|x64
        Release|x64 = Release|x64
    EndGlobalSection
    GlobalSection(ProjectConfigurationPlatforms) = postSolution
        {{{os.urandom(16).hex().upper()}}}.Debug|x64.ActiveCfg = Debug|x64
        {{{os.urandom(16).hex().upper()}}}.Debug|x64.Build.0 = Debug|x64
        {{{os.urandom(16).hex().upper()}}}.Release|x64.ActiveCfg = Release|x64
        {{{os.urandom(16).hex().upper()}}}.Release|x64.Build.0 = Release|x64
    EndGlobalSection
EndGlobal
'''

def get_main_cpp_content():
    return '''#include <Windows.h>
#include <iostream>

#include "SDK/Engine_classes.hpp"

// Basic.cpp was added to the VS project
// Engine_functions.cpp was added to the VS project

DWORD MainThread(HMODULE Module)
{
    /* Code to open a console window */
    AllocConsole();
    FILE* Dummy;
    freopen_s(&Dummy, "CONOUT$", "w", stdout);
    freopen_s(&Dummy, "CONIN$", "r", stdin);

    /* Functions returning "static" instances */
    SDK::UEngine* Engine = SDK::UEngine::GetEngine();
    SDK::UWorld* World = SDK::UWorld::GetWorld();

    /* Getting the PlayerController, World, OwningGameInstance, ... should all be checked not to be nullptr! */
    SDK::APlayerController* MyController = World->OwningGameInstance->LocalPlayers[0]->PlayerController;

    /* Print the full-name of an object ("ClassName PackageName.OptionalOuter.ObjectName") */
    std::cout << Engine->ConsoleClass->GetFullName() << std::endl;

    /* Manually iterating GObjects and printing the FullName of every UObject that is a Pawn (not recommended) */
    for (int i = 0; i < SDK::UObject::GObjects->Num(); i++)
    {
        SDK::UObject* Obj = SDK::UObject::GObjects->GetByIndex(i);

        if (!Obj)
            continue;

        if (!Obj->IsDefaultObject())
            continue;

        /* Only the 'IsA' check using the cast flags is required, the other 'IsA' is redundant */
        if (Obj->IsA(SDK::APawn::StaticClass()) || Obj->HasTypeFlag(SDK::EClassCastFlags::Pawn))
        {
            std::cout << Obj->GetFullName() << "\\n";
        }
    }

    /* You might need to loop all levels in UWorld::Levels */
    SDK::ULevel* Level = World->PersistentLevel;
    SDK::TArray<SDK::AActor*>& volatile Actors = Level->Actors;

    for (SDK::AActor* Actor : Actors)
    {
        /* The 2nd and 3rd checks are equal, prefer using EClassCastFlags if available for your class. */
        if (!Actor || !Actor->IsA(SDK::EClassCastFlags::Pawn) || !Actor->IsA(SDK::APawn::StaticClass()))
            continue;

        SDK::APawn* Pawn = static_cast<SDK::APawn*>(Actor);
        // Use Pawn here
    }

    /* 
    * Changes the keyboard-key that's used to open the UE console
    * 
    * This is a rare case of a DefaultObjects' member-variables being changed.
    * By default you do not want to use the DefaultObject, this is a rare exception.
    */
    SDK::UInputSettings::GetDefaultObj()->ConsoleKeys[0].KeyName = SDK::UKismetStringLibrary::Conv_StringToName(L"F2");

    /* Creates a new UObject of class-type specified by Engine->ConsoleClass */
    SDK::UObject* NewObject = SDK::UGameplayStatics::SpawnObject(Engine->ConsoleClass, Engine->GameViewport);

    /* The Object we created is a subclass of UConsole, so this cast is **safe**. */
    Engine->GameViewport->ViewportConsole = static_cast<SDK::UConsole*>(NewObject);

    return 0;
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD reason, LPVOID lpReserved)
{
    switch (reason)
    {
    case DLL_PROCESS_ATTACH:
        CreateThread(0, 0, (LPTHREAD_START_ROUTINE)MainThread, hModule, 0, 0);
        break;
    }

    return TRUE;
}
'''

