//
//  ChatListController.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit
import SwiftyJSON

class ChatListController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    @IBOutlet weak var tableView: UITableView!
    @IBOutlet weak var plusContainerView: UIView!
    
    let refreshControl: UIRefreshControl = UIRefreshControl()
    var chatListModel: ChatListModel = ChatListModel()
    
    // -----------------------------------
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        if !AuthHelper.isAuthorized {
            present(UIHelper.createAuthController(), animated: false, completion: nil)
        } else {
            updateAll()
        }
        
        uiSetup()
    }
    
    func uiSetup() {
        //UIHelper.createGradientOnView(view: plusContainerView, cornerRadius: 35.0)
        UIHelper.createColoredShadowOnView(view: plusContainerView)
        
        refreshControl.tintColor = UIHelper.pinkColor
        refreshControl.addTarget(self, action: #selector(updateAll), for: .valueChanged)
        
        tableView.refreshControl = refreshControl
    }
    
    // -----------------------------------
    
    func updateAll() {
        API.getUserList(completion: onChatListLoaded)
    }
    
    func onChatListLoaded(json: JSON) -> () {
        refreshControl.endRefreshing()
        chatListModel.setupWith(json: json)
        tableView.reloadData()
    }
    
    // -----------------------------------
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return AuthHelper.isAuthorized ? 1 : 0
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return chatListModel.list.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "chatCell", for: indexPath) as! ChatTableViewCell
        
        cell.chat = chatListModel.list[indexPath.row]
        
        return cell
        
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        performSegue(withIdentifier: "toChat", sender: indexPath)
    }
    
    // -----------------------------------
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "toChat" {
            let indexPath = sender as! IndexPath
            let chatController = segue.destination as! ChatViewController
            chatController.chat = chatListModel.list[indexPath.row]
        }
    }
    
    // -----------------------------------
    
    @IBAction func onPlus(_ sender: Any) {
        performSegue(withIdentifier: "toChoseUser", sender: nil)
    }
    
    // -----------------------------------
    
    override func motionEnded(_ motion: UIEventSubtype, with event: UIEvent?) {
        super.motionEnded(motion, with: event)
        if motion == .motionShake {
            AuthData.shared.id = nil
            AuthData.shared.token = nil
            //AuthHelper.isAuthorized = false
            present(UIHelper.createAuthController(), animated: false, completion: nil)
        }
    }
}
