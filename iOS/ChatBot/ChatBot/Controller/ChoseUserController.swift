//
//  ChoseUserController.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit
import SwiftyJSON

class ChoseUserController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    var userListModel: UserListModel = UserListModel()
    
    @IBOutlet weak var tableView: UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.contentInset = UIEdgeInsetsMake(64.0, 0.0, 0.0, 0.0)
        
        API.getUserList(completion: onUserListLoaded)
    }
    
    func onUserListLoaded(json: JSON) -> () {
        userListModel.setupWith(json: json)
        tableView.reloadData()
    }
    
    // --------------
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return userListModel.list.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "choseUserCell", for: indexPath) as! ChoseUserTableViewCell
        
        cell.user = userListModel.list[indexPath.row]
        
        return cell
    }
    
    // --------------
    
    @IBAction func onCancel(_ sender: Any) {
        dismiss(animated: true, completion: nil)
    }
}
