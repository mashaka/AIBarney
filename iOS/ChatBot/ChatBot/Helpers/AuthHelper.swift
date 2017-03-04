//
//  AuthHelper.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation

class AuthHelper {
    static let shared: AuthHelper = AuthHelper()
    
    var isAuthorized: Bool = {
        return false
    }()
    
    
}
