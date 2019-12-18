def write(self, vals):
    change_dict = {}
    # 修改管理项目
    if 'work_description' in vals:
        """
        创建作业指导票修订记录
        """
        work_desr_old = re.findall(r'<p>(.*?)</p>', self.work_description)
        work_desr_new = re.findall(r'<p>(.*?)</p>', vals['work_description'])
        change = '<p>管理项目变更前：</p>'
        for old in work_desr_old:
            if old in work_desr_new:
                work_desr_new.remove(old)
            else:
                if old != '<br>':
                    change = change + '<p>&nbsp;&nbsp;&nbsp;&nbsp;' + old + '</p>'
        # 如果没有变更，添加了新的
        if change == '<p>管理项目变更前：</p>':
            change = '<p>新增管理项目：</p>'
        else:
            change = change + '<p>管理项目变更后：</p>'
        for new in work_desr_new:
            if new != '<br>':
                change = change + '<p>&nbsp;&nbsp;&nbsp;&nbsp;' + new + '</p>'
        change_dict['contents'] = change
    #  修改作业内容
    if 'work_content' in vals:
        change_dict['work_content'] = vals['work_content']
        if 'contents' not in change_dict:
            change_dict['contents'] = ''
        change_dict['contents'] = change_dict['contents'] + "<p>作业内容变更前：" + self.work_content + "</p><p>作业内容变更后：" + vals['work_content'] + '</p>'
    # 修改作业项目名称
    if 'work_subject' in vals:
        if 'contents' not in change_dict:
            change_dict['contents'] = ''
        change_dict['contents'] = change_dict['contents'] + "<p>作业项目变更前：" + self.work_subject + "</p><p>作业项目变更后：" + vals['work_subject'] + '</p>'
    # 修改了作业关键点
    if 'key_point' in vals:
        if 'contents' not in change_dict:
            change_dict['contents'] = ''
        change_dict['contents'] = change_dict['contents'] + "<p>关键点变更前：" + self.key_point + "</p><p>关键点变更后：" + vals['key_point'] + '</p>'

    if change_dict:
        if not change_dict.get('work_content', None):
            change_dict['work_content'] = self.work_content
        change_dict['subject_no'] = str(self.subject_no)
        change_dict['instruction_id'] = self.instruction_id.id
        self.env['toto.qc.work.inst.revision.history'].create(change_dict)
    super(QcWorkInstructionItem, self).write(vals)

def unlink(self):
    for item in self:
        if item.work_subject:
            self.env['toto.qc.work.inst.revision.history'].create({
                'subject_no': str(item.subject_no),
                'work_content': item.work_content,
                'instruction_id': item.instruction_id.id,
                'contents': "<p>删除删除作业内容：" + item.work_content + "</p>"
            })
    super(QcWorkInstructionItem, self).unlink()
