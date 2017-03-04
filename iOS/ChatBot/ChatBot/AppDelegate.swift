//
//  AppDelegate.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        
        UIHelper.shared.setNavBarAppearance()
        
        return true
    }

    func application(_ application: UIApplication, handleOpen url: URL) -> Bool {
        if url.scheme == "chatbot" {
            _ = AuthData.shared.setFromQuery(query: url.query!)
        }
        return true
    }

}

