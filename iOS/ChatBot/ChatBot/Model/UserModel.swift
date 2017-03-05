//
//  UserModel.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation
import SwiftyJSON

struct User {
    var id: String
    var avatarUrl: URL?
    var firstname: String
    var lastname: String
    
    init(id: String,
         avatarUrl: URL?,
         firstname: String,
         lastname: String) {
        self.id = id
        self.avatarUrl = avatarUrl
        self.firstname = firstname
        self.lastname  = lastname
    }
    
    init(json: JSON) {
        self.id = json["id"].stringValue
        self.avatarUrl = URL(string: json["avatar_url"].stringValue)
        self.firstname = json["first_name"].stringValue
        self.lastname = json["last_name"].stringValue
    }
    
    static var mockUser: User = {
        return User(id: "1", avatarUrl: URL(string: "empty"), firstname: "Alexey", lastname: "Zhuravlev")
    }()
}
