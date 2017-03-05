//
//  TipViewController.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 05/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit
import SwipeCellKit

class TipViewController: UIViewController, UITableViewDelegate, UITableViewDataSource, SwipeTableViewCellDelegate {
    
    var chatId: String?
    var intersection: Intersection?
    
    @IBOutlet weak var tableView: UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.contentInset = UIEdgeInsetsMake(6.0, 0.0, 0.0, 0.0)
        
        tableView.estimatedRowHeight = 70.0
        tableView.rowHeight = UITableViewAutomaticDimension
    }
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return intersection == nil ? 0 : intersection!.tips.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "tipMessageCell", for: indexPath) as! TipMessageTableViewCell
        
        cell.tip = intersection!.tips[indexPath.row]
        cell.delegate = self
        
        return cell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        
        dismiss(animated: true) { 
            let chatController = Router.getTopMostVisibleController() as! ChatViewController
            chatController.usedTipId = self.intersection!.tips[indexPath.row].algoId
            chatController.newMessageTextView.text = self.intersection!.tips[indexPath.row].text
        }
    }
    
    func tableView(_ tableView: UITableView, editActionsForRowAt indexPath: IndexPath, for orientation: SwipeActionsOrientation) -> [SwipeAction]? {
        if orientation != .right { return nil }
        
        let deleteAction = SwipeAction(style: .destructive, title: "Remove") { (action, indexPath) in
            API.deleteTip(chatId: self.chatId!, algoId: self.intersection!.tips[indexPath.row].algoId)
            
            self.intersection!.tips.remove(at: indexPath.row)
            self.tableView.beginUpdates()
            self.tableView.deleteRows(at: [indexPath], with: .fade)
            self.tableView.endUpdates()
        }
        
        deleteAction.font = UIHelper.shared.barButtonFont()
        deleteAction.backgroundColor = UIHelper.pinkColor
        
        return [deleteAction]
    }
}
