// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME DictDict
#define R__NO_DEPRECATION

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "ROOT/RConfig.hxx"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// Header files passed as explicit arguments
#include "DictTypes.h"

// Header files passed via #pragma extra_include

// The generated code does not explicitly qualify STL entities
namespace std {} using namespace std;

namespace ROOT {
   static TClass *ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR_Dictionary();
   static void ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR_TClassManip(TClass*);
   static void *new_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR(void *p = nullptr);
   static void *newArray_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR(Long_t size, void *p);
   static void delete_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR(void *p);
   static void deleteArray_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR(void *p);
   static void destruct_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >*)
   {
      ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > > *ptr = nullptr;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >));
      static ::ROOT::TGenericClassInfo 
         instance("ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >", -2, "ROOT/RVec.hxx", 1529,
                  typeid(ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR_Dictionary, isa_proxy, 4,
                  sizeof(ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >) );
      instance.SetNew(&new_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR);
      instance.SetNewArray(&newArray_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR);
      instance.SetDelete(&delete_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR);
      instance.SetDeleteArray(&deleteArray_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR);
      instance.SetDestructor(&destruct_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > > >()));
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >*)
   {
      return GenerateInitInstanceLocal(static_cast<ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >*>(nullptr));
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal(static_cast<const ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >*>(nullptr)); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal(static_cast<const ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >*>(nullptr))->GetClass();
      ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR(void *p) {
      return  p ? ::new(static_cast<::ROOT::Internal::TOperatorNewHelper*>(p)) ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > > : new ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >;
   }
   static void *newArray_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR(Long_t nElements, void *p) {
      return p ? ::new(static_cast<::ROOT::Internal::TOperatorNewHelper*>(p)) ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >[nElements] : new ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >[nElements];
   }
   // Wrapper around operator delete
   static void delete_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR(void *p) {
      delete (static_cast<ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >*>(p));
   }
   static void deleteArray_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR(void *p) {
      delete [] (static_cast<ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >*>(p));
   }
   static void destruct_ROOTcLcLVecOpscLcLRVeclEROOTcLcLMathcLcLLorentzVectorlEROOTcLcLMathcLcLPxPyPzE4DlEfloatgRsPgRsPgR(void *p) {
      typedef ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > > current_t;
      (static_cast<current_t*>(p))->~current_t();
   }
} // end of namespace ROOT for class ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >

namespace {
  void TriggerDictionaryInitialization_DictDict_Impl() {
    static const char* headers[] = {
"DictTypes.h",
nullptr
    };
    static const char* includePaths[] = {
"/usr/include",
"/home/sunbaee_/Documents/Scripts/Python/Projects/GASP/dataSlicer/TMVA/",
nullptr
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "DictDict dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_AutoLoading_Map;
namespace ROOT{namespace Math{template <class ScalarType = double> class __attribute__((annotate("$clingAutoload$Math/GenVector/PxPyPzE4D.h")))  __attribute__((annotate("$clingAutoload$DictTypes.h")))  PxPyPzE4D;
}}
namespace ROOT{namespace Math{template <class CoordSystem> class __attribute__((annotate("$clingAutoload$Math/Vector4Dfwd.h")))  __attribute__((annotate("$clingAutoload$DictTypes.h")))  LorentzVector;
}}
namespace ROOT{namespace VecOps{template <typename T> class __attribute__((annotate(R"ATTRDUMP(__cling__ptrcheck(off))ATTRDUMP"))) __attribute__((annotate("$clingAutoload$ROOT/RVec.hxx")))  __attribute__((annotate("$clingAutoload$DictTypes.h")))  RVec;
}}
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "DictDict dictionary payload"


#define _BACKWARD_BACKWARD_WARNING_H
// Inline headers
#include "DictTypes.h"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[] = {
"ROOT::VecOps::RVec<ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > >", payloadCode, "@",
nullptr
};
    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("DictDict",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_DictDict_Impl, {}, classesHeaders, /*hasCxxModule*/false);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_DictDict_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_DictDict() {
  TriggerDictionaryInitialization_DictDict_Impl();
}
