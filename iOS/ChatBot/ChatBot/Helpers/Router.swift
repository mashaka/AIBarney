//
//  Router.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation
import UIKit

class Router {
    static let shared = Router()
    
    static func getTopNavigationController() -> UINavigationController {
        var result: UIViewController = UIApplication.shared.keyWindow!.rootViewController!
        
        while result.presentedViewController != nil {
            result = result.presentedViewController!
        }
        
        let topNavigationController: UINavigationController = result.isKind(of: UINavigationController.classForCoder()) ? result as! UINavigationController : result.navigationController!
        
        return topNavigationController
    }
    
    static func getTopMostVisibleController() -> UIViewController {
        var result: UIViewController = UIApplication.shared.keyWindow!.rootViewController!
        
        while result.presentedViewController != nil {
            result = result.presentedViewController!
        }
        
        if(result.isKind(of: UINavigationController.classForCoder())) {
            if((result as! UINavigationController).topViewController == nil) { return result }
            result = (result as! UINavigationController).topViewController!
        }
        
        return result
    }
}
