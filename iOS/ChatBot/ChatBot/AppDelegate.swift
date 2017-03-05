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
        window?.backgroundColor = UIColor.white
        
        return true
    }

    func application(_ application: UIApplication, handleOpen url: URL) -> Bool {
        if url.scheme == "chatbot" {
            if AuthData.shared.setFromQuery(query: url.query!) {
                DispatchQueue.main.async {
                    Router.getTopMostVisibleController().dismiss(animated: true, completion: {
                        let chat = Router.getTopMostVisibleController() as! ChatListController
                        chat.updateAll()
                    })
                }
            }
        }
        return true
    }

}

