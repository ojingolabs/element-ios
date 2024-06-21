// 
// Copyright 2024 New Vector Ltd
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
/*
 Never import this file in header files (.h) only in implementation files (.m).
 If you want to reference a Swift class from the project please use forward declaration in the header file and then import this header in your implementation file.
*/

#ifndef RiotSwiftHeader_h
#define RiotSwiftHeader_h

#if __has_include(<ElementRiot/GeneratedInterface-Swift.h>)
    #import <ElementRiot/GeneratedInterface-Swift.h>
#elif __has_include("GeneratedInterface-Swift")
    #import "GeneratedInterface-Swift.h"
#endif

#endif /* RiotSwiftHeader_h */
