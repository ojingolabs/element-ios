/*
 Copyright 2017 Vector Creations Ltd
 
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 
 http://www.apache.org/licenses/LICENSE-2.0
 
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 */

#import "EventDetailsView.h"

#import "ThemeService.h"
#import "RiotSwiftHeader.h"

@implementation EventDetailsView

-(void)customizeViewRendering
{
    [super customizeViewRendering];
    
    self.backgroundColor = ThemeService.shared.theme.headerBackgroundColor;
    self.textView.backgroundColor = ThemeService.shared.theme.backgroundColor;
    self.textView.textColor = ThemeService.shared.theme.textPrimaryColor;
    self.redactButton.tintColor = ThemeService.shared.theme.tintColor;
    self.closeButton.tintColor = ThemeService.shared.theme.tintColor;
}

@end
