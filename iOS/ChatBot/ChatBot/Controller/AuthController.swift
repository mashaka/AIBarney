//
//  AuthController.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit

class AuthController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        navigationController?.setNavigationBarHidden(true, animated: false)
        
        UIHelper.createGradientOnView(view: view)
    }
    
    @IBAction func onLogin(_ sender: Any) {
        dismiss(animated: true, completion: nil)
    }
}
