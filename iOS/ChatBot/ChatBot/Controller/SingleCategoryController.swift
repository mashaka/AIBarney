//
//  SingleCategoryController.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 05/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit

class SingleCategoryController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    
    var chatId: String?
    var category: Category?
    
    var headerView: ColorTypeHeaderView!
    
    @IBOutlet weak var tableView: UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.heroModifiers = [.cascade]
        
        title = category!.categoryType.name()
        
        headerView = ColorTypeHeaderView(frame: CGRect(x: 0, y: 0, width: UIScreen.main.bounds.width, height: 150.0))
        headerView.imageView.image = category!.categoryType.image()
        headerView.imageView.heroID = "\(category!.categoryType.name())_image"
        headerView.heroID = "\(category!.categoryType.name())_container"
        headerView.heroModifiers = [.cornerRadius(0.0)]
        
        tableView.tableHeaderView = headerView
        tableView.heroModifiers = [.cascade]
        
        tableView.estimatedRowHeight = 70.0
        tableView.rowHeight = UITableViewAutomaticDimension
    }
    
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return category == nil ? 0 : category!.intersections.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "intersectionCell", for: indexPath) as! IntersectionTableViewCell
        
        cell.intersection = category!.intersections[indexPath.row]
        cell.heroModifiers = [.fade, .scale(0.5)]
        
        return cell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        performSegue(withIdentifier: "toIntersection", sender: indexPath)
    }
    
    func scrollViewDidScroll(_ scrollView: UIScrollView) {
        headerView.scrollViewDidScroll(scrollView: scrollView)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "toIntersection" {
            let indexPath = sender as! IndexPath
            (segue.destination as! TipViewController).intersection = category!.intersections[indexPath.row]
            (segue.destination as! TipViewController).chatId = chatId
        }
    }
}
