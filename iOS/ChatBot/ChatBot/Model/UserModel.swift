//
//  UserModel.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation

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
}
