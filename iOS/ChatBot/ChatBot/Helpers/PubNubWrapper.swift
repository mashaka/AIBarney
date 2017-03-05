//
//  PubNubWrapper.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation
import PubNub

class PubNubWrapper {
    static let shared: PubNubWrapper = PubNubWrapper()
    
    var client: PubNub!
    
    init() {
        let configuration = PNConfiguration(publishKey: "pub-c-8465dadc-3bc2-40be-a68d-16110286f809", subscribeKey: "sub-c-51962ec8-0100-11e7-8437-0619f8945a4f")
        client = PubNub.clientWithConfiguration(configuration)
    }
}
