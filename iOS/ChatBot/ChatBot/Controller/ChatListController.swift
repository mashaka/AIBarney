//
//  ChatListController.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit

class ChatListController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    @IBOutlet weak var plusContainerView: UIView!
    
    // -----------------------------------
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        if !AuthHelper.shared.isAuthorized {
            present(UIHelper.createAuthController(), animated: false, completion: nil)
        }
        
        uiSetup()
    }
    
    func uiSetup() {
        UIHelper.createGradientOnView(view: plusContainerView, cornerRadius: 35.0)
        UIHelper.createColoredShadowOnView(view: plusContainerView)
    }
    
    // -----------------------------------
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return AuthHelper.shared.isAuthorized ? 0 : 0
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 0
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        return UITableViewCell()
    }
    
    // -----------------------------------
    
    @IBAction func onPlus(_ sender: Any) {
        performSegue(withIdentifier: "toChoseUser", sender: nil)
    }
}
