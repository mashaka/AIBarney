//
//  ChatListModel.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation
import SwiftyJSON

struct ChatListModel {
    var list: [Chat] = []
    
    mutating func setupWith(json: JSON) {
        list.removeAll()
        for jsonElement in json.arrayValue {
            let user = User(json: jsonElement)
            if jsonElement["has_chat"].boolValue {
                list.append(Chat(json: jsonElement["chat"], partner: user))
            }
        }
    }
}
