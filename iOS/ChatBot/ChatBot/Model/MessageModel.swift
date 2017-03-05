//
//  MessageModel.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation
import SwiftyJSON

struct Message {
    var text: String
    var id: String
    var date: Date
    var author: User
    
    init(text: String) {
        self.text = text
        self.date = Date()
        
        self.id = ""
        self.author = User(id: AuthData.shared.id!, avatarUrl: nil, firstname: "", lastname: "")
    }
    
    init?(json: JSON, author: User) {
        if json.isEmpty {
            return nil
        }
        
        self.author = author
        self.text = json["text"].stringValue
        self.date = json["add_time"].stringValue.dateFromISO8601!
        self.id = json["id"].stringValue
    }
    
    init(json: JSON?) {
        self.author = User(json: json!["author"])
        self.text = json!["text"].stringValue
        self.date = json!["add_time"].stringValue.dateFromISO8601!
        self.id = json!["id"].stringValue
    }
    
    func apiParams() -> [String: String] {
        return ["text": text]
    }
}
